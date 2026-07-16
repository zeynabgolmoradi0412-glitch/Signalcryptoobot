import ccxt
from config import TIMEFRAME

exchange = ccxt.binance({
    "enableRateLimit": True
})

def get_usdt_pairs():
    markets = exchange.load_markets()

    pairs = []

    for symbol in markets:
        if symbol.endswith("/USDT"):
            pairs.append(symbol)

    return pairs


def get_ohlcv(symbol, limit=200):
    return exchange.fetch_ohlcv(
        symbol,
        timeframe=TIMEFRAME,
        limit=limit
    )
