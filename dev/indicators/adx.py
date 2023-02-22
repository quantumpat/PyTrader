import pandas as pd
import pandas_ta as ta
import yfinance
import datetime
import robin_stocks.robinhood as rh


def get_adx(ticker):
    stock_data = yfinance.download(ticker, interval="1m", start=str(datetime.date.today() - datetime.timedelta(5)),
                                   end=str(datetime.date.today()))

    total_adx = ta.adx(stock_data["High"], stock_data["Low"], stock_data["Close"], length=14)

    class adxData:
        def __init__(self, adx):
            self.adx = adx['ADX_14']
            self.last_adx = self.adx.iloc[-1]
            self.dmi_positive = adx['DMP_14']
            self.dmi_negative = adx['DMN_14']
            self.last_dmi_negative = self.dmi_negative.iloc[-1]
            self.last_dmi_positive = self.dmi_positive.iloc[-1]

    adx = adxData(total_adx)

    return adx



