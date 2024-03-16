import ccxt

binance = ccxt.binance()
markets = binance.load_markets()
btc_ticker = binance.fetch_ticker('AVAX/USD')
print(btc_ticker)

