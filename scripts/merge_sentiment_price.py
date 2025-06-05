import pandas as pd
import os

def merge_sentiment_and_price(price_file, sentiment_file, output_file='data/merged_data.csv'):
    if not os.path.exists(price_file) or not os.path.exists(sentiment_file):
        print("❌ Missing input files.")
        return

    # Load stock price data
    price_df = pd.read_csv(price_file, parse_dates=['Date'])
    price_df = price_df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

    # Load sentiment data
    sentiment_df = pd.read_csv(sentiment_file, parse_dates=['datetime'])

    # Aggregate sentiment by date
    sentiment_df['date_only'] = sentiment_df['datetime'].dt.date
    daily_sentiment = sentiment_df.groupby('date_only')['compound'].mean().reset_index()
    daily_sentiment.rename(columns={'date_only': 'Date', 'compound': 'avg_sentiment'}, inplace=True)
    daily_sentiment['Date'] = pd.to_datetime(daily_sentiment['Date'])

    # Merge on date
    merged_df = pd.merge(price_df, daily_sentiment, on='Date', how='left')
    merged_df.sort_values(by='Date', inplace=True)

    # Fill missing sentiment with 0 (neutral)
    merged_df['avg_sentiment'] = merged_df['avg_sentiment'].fillna(0)

    # Optional: Generate a basic signal
    merged_df['signal'] = merged_df['avg_sentiment'].apply(
        lambda x: 'Buy' if x > 0.2 else ('Sell' if x < -0.2 else 'Hold')
    )

    merged_df.to_csv(output_file, index=False)
    print(f"✅ Merged data saved to {output_file}")

# Example usage
if __name__ == "__main__":
    merge_sentiment_and_price(
        price_file='data/TCS.NS_price_data.csv',
        sentiment_file='data/tweets_sentiment.csv'
    )

