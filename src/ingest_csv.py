import pandas as pd
import re
import argparse
from utils import get_connection

def extract_hashtags(text):
    return re.findall(r"#(\w+)", text.lower())

def ingest(csv_file):
    conn = get_connection()
    cur = conn.cursor()

    # ✅ Clear child table first, then parent
    cur.execute("DELETE FROM hashtags;")
    cur.execute("DELETE FROM tweets;")

    df = pd.read_csv(csv_file)
    for _, row in df.iterrows():
        cur.execute(
            "REPLACE INTO tweets (tweet_id, user_name, text, created_at) VALUES (%s, %s, %s, %s)",
            (row['tweet_id'], row['user_name'], row['text'], row['created_at'])
        )
        hashtags = extract_hashtags(row['text'])
        for ht in hashtags:
            cur.execute(
                "INSERT INTO hashtags (tweet_id, hashtag, created_at) VALUES (%s, %s, %s)",
                (row['tweet_id'], ht, row['created_at'])
            )
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True)
    args = parser.parse_args()
    ingest(args.csv)
