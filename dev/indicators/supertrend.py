import pandas as pd
import pandas_ta as ta
import yfinance
import datetime
import robin_stocks.robinhood as rh



def get_supertrend(ticker, length, multiplier):


    stock_data = yfinance.download(ticker, interval="1m", start=str(datetime.date.today() - datetime.timedelta(5)),
                                   end=str(datetime.date.today()))

    supertrend_length = length
    supertrend_multiplier = multiplier

    supertrend_longtext = f'SUPERTl_{supertrend_length}_{supertrend_multiplier}.0'
    supertrend_shorttext = f'SUPERTs_{supertrend_length}_{supertrend_multiplier}.0'

    supertrend = ta.supertrend(stock_data['High'], stock_data['Low'], stock_data['Close'], length=supertrend_length, multiplier=supertrend_multiplier)

    class SUPERTRENDDATA:
        def __init__(self):
            self.length = length
            self.multiplier = multiplier
            self.long_signals = supertrend_length[supertrend_longtext]
            self.short_signals = supertrend_length[supertrend_shorttext]
            self.supertrend_all = supertrend

    return SUPERTRENDDATA



