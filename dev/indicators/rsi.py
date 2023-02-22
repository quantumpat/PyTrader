
import pandas_ta as pta
import yfinance
import datetime

def get_rsi(ticker):
    stock_data = yfinance.download(ticker, str(datetime.date.today() - datetime.timedelta(21)), str(datetime.date.today()))
    total_rsi = pta.rsi(stock_data["Close"], length=14)
    last_rsi = total_rsi.iloc[-1]

    return last_rsi