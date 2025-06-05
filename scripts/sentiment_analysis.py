import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

def analyze_sentiment(input_file='data/tweets.csv', output_file='data/tweets_sentiment.csv'):
    if not os.path.exists(input_file):
        print(f"❌ Input file not found: {input_file}")
        return

    df = pd.read_csv(input_file)

    analyzer = SentimentIntensityAnalyzer()

    sentiments = []
    for text in df['text']:
        scores = analyzer.polarity_scores(str(text))
        sentiments.append(scores)

    sentiment_df = pd.DataFrame(sentiments)
    result_df = pd.concat([df, sentiment_df], axis=1)

    # Label sentiment
    result_df['sentiment_label'] = result_df['compound'].apply(
        lambda x: 'positive' if x > 0.05 else ('negative' if x < -0.05 else 'neutral')
    )

    result_df.to_csv(output_file, index=False)
    print(f"✅ Sentiment analysis complete. Output saved to {output_file}")

# Example usage
if __name__ == "__main__":
    analyze_sentiment()
