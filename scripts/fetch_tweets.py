import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime, timedelta
import os

def fetch_tweets(query, days_back=7, max_tweets=1000, filename="tweets.csv"):
    since_date = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')
    print(f"🔍 Scraping tweets for: '{query}' since {since_date}")

    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{query} since:{since_date}').get_items()):
        if i >= max_tweets:
            break
        tweets.append([tweet.date, tweet.content, tweet.user.username])

    df = pd.DataFrame(tweets, columns=['datetime', 'text', 'user'])
    
    os.makedirs("data", exist_ok=True)
    df.to_csv(f"E:/GIT Projects/Stock Market Sentiment & Price Analysis/data/{filename}", index=False)
    print(f"✅ Saved {len(df)} tweets to data/{filename}")

# Example usage
if __name__ == "__main__":
    fetch_tweets("TCS stock OR TCS shares OR Tata Consultancy Services", days_back=7, max_tweets=500)

