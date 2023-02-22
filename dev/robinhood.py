
from indicators.rsi import get_rsi

import robin_stocks.robinhood as robin

login = robin.login("patrick.carroll3322@gmail.com", "Patrick51090!")

print(get_rsi("AAPL").last_rsi)