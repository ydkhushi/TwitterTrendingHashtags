CREATE DATABASE IF NOT EXISTS twitter_trends;
USE twitter_trends;

CREATE TABLE IF NOT EXISTS tweets (
    tweet_id BIGINT PRIMARY KEY,
    user_name VARCHAR(50),
    text TEXT,
    created_at DATETIME
);

CREATE TABLE IF NOT EXISTS hashtags (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    tweet_id BIGINT,
    hashtag VARCHAR(100),
    created_at DATETIME,
    FOREIGN KEY (tweet_id) REFERENCES tweets(tweet_id)
);

CREATE TABLE IF NOT EXISTS top_hashtags (
    hashtag VARCHAR(100),
    total_count INT,
    PRIMARY KEY (hashtag)
);

CREATE TABLE IF NOT EXISTS hashtag_counts_hourly (
    hashtag VARCHAR(100),
    window_start DATETIME,
    count INT,
    PRIMARY KEY (hashtag, window_start)
);

-- ALTER USER 'root'@'localhost' IDENTIFIED BY 'NewStrongPassword123!';
