
import pandas_ta as ta
import yfinance
import datetime

def get_rsi(ticker):
    stock_data = yfinance.download(ticker, str(datetime.date.today() - datetime.timedelta(21)), str(datetime.date.today()))
    total_rsi = ta.rsi(stock_data["Close"], length=14)


    class rsiData:
        def __init__(self, rsi):
            self.rsi = rsi
            self.last_rsi = rsi.iloc[-1]

    rsi = rsiData(total_rsi)

    return rsi