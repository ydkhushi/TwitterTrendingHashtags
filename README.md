
# Twitter Trending Hashtag Project

A Python-based project that extracts and analyzes trending hashtags on Twitter using the Twitter API, performs ETL (Extract, Transform, Load) operations, and stores the data in a MySQL database. This project helps understand trending topics in real-time and visualize insights effectively.

## Features

* Fetches real-time trending hashtags from Twitter.
* Stores historical trends in a MySQL database for analysis.
* Performs ETL operations to clean and transform data.
* Generates analytical insights such as most frequent hashtags, trends by region, and trending topics over time.
* Can be extended to visualize trends using Power BI or Python libraries like Matplotlib/Seaborn.

## Tech Stack

* **Python**: Main programming language.
* **Tweepy / Twitter API**: Fetch trending hashtags and tweets.
* **MySQL**: Database for storing trends and analytics data.
* **Pandas**: Data cleaning and transformation.
* **Matplotlib / Seaborn** (optional): Data visualization.
* **VS Code**: IDE used for development.

## Project Structure

```
twitter-trending-hashtag/
│
├── data/                  # Optional folder to store exported CSV files
├── scripts/               # Python scripts for ETL and analysis
│   ├── fetch_trends.py    # Script to fetch trends from Twitter API
│   ├── transform_data.py  # Script to clean and prepare data
│   └── load_to_mysql.py   # Script to load data into MySQL
├── .env                   # Environment variables (API keys, DB credentials)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/twitter-trending-hashtag.git
   cd twitter-trending-hashtag
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables in `.env` file:

   ```
   TWITTER_API_KEY=your_api_key
   TWITTER_API_SECRET=your_api_secret
   TWITTER_ACCESS_TOKEN=your_access_token
   TWITTER_ACCESS_SECRET=your_access_secret
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASSWORD=yourpassword
   MYSQL_DB=twitter_trends
   ```

5. Run the ETL pipeline:

   ```bash
   python scripts/fetch_trends.py
   python scripts/transform_data.py
   python scripts/load_to_mysql.py
   ```

## Usage

* Fetch trends for a specific location by updating the `WOEID` (Where On Earth ID) in `fetch_trends.py`.
* Use the database to query top hashtags over time or region.
* Optional: Connect Power BI or other visualization tools to the MySQL database for interactive dashboards.

## Future Enhancements

* Automate the ETL pipeline to run at regular intervals using `cron` or `Airflow`.
* Add sentiment analysis for trending hashtags.
* Add dashboard visualizations using Plotly or Power BI.

## Contributing

Contributions are welcome! Please create a pull request or raise issues for suggestions.

