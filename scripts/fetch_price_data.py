import yfinance as yf
import pandas as pd
from datetime import datetime

def fetch_stock_data(ticker, start_date="2023-01-01", end_date=None, interval="1d"):
    if not end_date:
        end_date = datetime.now().strftime('%Y-%m-%d')

    print(f"Fetching data for {ticker} from {start_date} to {end_date}...")

    df = yf.download(ticker, start=start_date, end=end_date, interval=interval,auto_adjust=False)
    df.reset_index(inplace=True)
    df.to_csv(f"E:/GIT Projects/Stock Market Sentiment & Price Analysis/data/{ticker}_price_data.csv", index=False)

    print(f"✅ Data saved to data/{ticker}_price_data.csv")

# Example usage
if __name__ == "__main__":
    fetch_stock_data("TCS.NS")  # You can change this to any NSE/BSE symbol on Yahoo
