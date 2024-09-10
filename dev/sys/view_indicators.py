from dev.indicators.adx import get_adx
from dev.indicators.rsi import get_rsi

ticker = 'NVDA'

print(f'RSI: {get_rsi(ticker).last_rsi}')

print(f'ADX: {get_adx(ticker).last_adx}')

