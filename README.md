# PyTrader
A python based trading program.

### Current Available Indicators

#### RSI
RSI or Relative Strength Index represents whether the stock is overbought or oversold. If the RSI value is between 0 to 30 the RSI indicates the stock is oversold, if the RSI value is between 70 and 100 the RSI indicates the stock is overbought.

```python
# Returns the rsi object
# Parameter 1: Ticker, the ticker symbol of the stock
get_rsi("[ticker]")

# To get the RSI as a number
get_rsi("[ticker]").last_rsi
```

#### ADX
ADX or Average Directional Movement Index represents the strength of a trend.

```python
# Returns the adx object
# Parameter 1: Ticker, the ticker symbol of the stock
get_adx("ticker")
```