
import robin_stocks.robinhood as robinhood
from indicators.rsi import get_rsi

# Keep this login info private!
login = robinhood.login("patrick.carroll3322@gmail.com", "Patrick51090!")

print(get_rsi("AAPL"))
