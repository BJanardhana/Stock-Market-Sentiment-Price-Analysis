# 📊 Stock Market Sentiment & Price Analysis

This project analyzes the relationship between **public sentiment on Twitter** and **stock price movements** using Python. It uses historical stock data and sentiment scores from tweets to generate trading signals like **Buy**, **Sell**, and **Hold**.

---

## 📁 Project Structure

```
stock-sentiment-price-analysis/
├── data/                     # CSV files for price, tweets, sentiment, merged data
├── notebooks/
│   └── analysis.ipynb        # Final data exploration & visualization notebook
├── scripts/
│   ├── fetch_price_data.py         # Get stock data using yfinance
│   ├── fetch_tweets.py             # Scrape tweets using snscrape
│   ├── sentiment_analysis.py       # Run VADER sentiment analysis
│   └── merge_sentiment_price.py    # Merge sentiment with price data
├── README.md
├── requirements.txt
└── LICENSE
```

---

## 🚀 Features

- ✅ Download stock data using `yfinance`
- ✅ Scrape Twitter sentiment using `snscrape` (no API key needed)
- ✅ Perform sentiment analysis with `VADER`
- ✅ Merge sentiment with price to detect trade signals
- ✅ Visualize trends, signals, and strategy performance

---

## 📊 Example Output

| Date       | Close | avg_sentiment | signal |
|------------|-------|----------------|--------|
| 2025-06-01 | 3425  | 0.45           | Buy    |
| 2025-06-02 | 3440  | -0.11          | Hold   |
| 2025-06-03 | 3410  | -0.42          | Sell   |

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/stock-sentiment-price-analysis.git
cd stock-sentiment-price-analysis

pip install -r requirements.txt
```

---

## 📌 Requirements

- Python 3.10+
- pandas
- matplotlib
- seaborn
- yfinance
- vaderSentiment
- snscrape (recommended with Python 3.10)

---

## 🧠 Usage

```bash
# 1. Fetch historical stock prices
python scripts/fetch_price_data.py

# 2. Scrape tweets about the stock
python scripts/fetch_tweets.py

# 3. Analyze sentiment of tweets
python scripts/sentiment_analysis.py

# 4. Merge sentiment and price data
python scripts/merge_sentiment_price.py

# 5. Visualize insights in Jupyter Notebook
jupyter notebook notebooks/analysis.ipynb
```

---

## 📝 License

This project is licensed under the MIT License. See `LICENSE` for details.
