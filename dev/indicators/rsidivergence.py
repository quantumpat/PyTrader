import pandas as pd
import pandas_ta as ta
import yfinance
import datetime
import robin_stocks.robinhood as rh

def get_rsidivergence(ticker):

    stock_data = yfinance.download(ticker, interval="1m", start=str(datetime.date.today() - datetime.timedelta(5)),
                                   end=str(datetime.date.today()))




    slow_rsi = ta.rsi(stock_data['Close'], length=21)
    fast_rsi = ta.rsi(stock_data['Close'], length=14)



    class RSIDIVERGENCEDATA:
        def __init__(self, adx):
            self.fast_rsi = fast_rsi
            self.slow_rsi = slow_rsi
            self.last_rsi_fast = self.fast_rsi[-1]
            self.last2nd_rsi_fast = self.fast_rsi[-2]
            self.last_rsi_slow = self.slow_rsi[-1]
            self.last2nd_rsi_slow = self.slow_rsi[-2]


    return RSIDIVERGENCEDATA




