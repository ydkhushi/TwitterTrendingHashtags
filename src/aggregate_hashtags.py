import argparse
from utils import get_connection

def aggregate(window_mins):
    conn = get_connection()
    cur = conn.cursor()

    # Top hashtags (global)
    cur.execute("TRUNCATE TABLE top_hashtags")
    cur.execute(
        """
        INSERT INTO top_hashtags (hashtag, total_count)
        SELECT hashtag, COUNT(*) as cnt
        FROM hashtags
        GROUP BY hashtag
        ORDER BY cnt DESC
        """
    )

    # Hourly/windowed counts
    cur.execute("TRUNCATE TABLE hashtag_counts_hourly")
    cur.execute(
        """
        INSERT INTO hashtag_counts_hourly (hashtag, window_start, count)
        SELECT hashtag,
               STR_TO_DATE(DATE_FORMAT(created_at, '%Y-%m-%d %H:00:00'), '%Y-%m-%d %H:%i:%s') as window_start,
               COUNT(*)
        FROM hashtags
        GROUP BY hashtag, window_start
        """
    )

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--window-mins", type=int, default=60)
    args = parser.parse_args()
    aggregate(args.window_mins)
