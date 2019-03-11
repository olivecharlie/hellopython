import requests
import json
import datetime

BINANCE_BASE_URL = 'https://api.binance.com'
ENDPOINT_AVG_PRICE = '/api/v3/avgPrice'
#ENDPOINT_AVG_PRICE = '/api/v1/ticker/24hr'
ENDPOINT_ALL_PRICES = '/api/v1/ticker/allPrices'
QS = 'symbol={symbol}'
URL = '{base_url}{endpoint}?{query_string}'

symbol = 'TRXBTC'

query_string = '' #QS_KLINES.format(symbol=symbol)

url = URL.format(base_url=BINANCE_BASE_URL,
								endpoint=ENDPOINT_ALL_PRICES, 
								query_string=query_string)

print(f'URL: {url}')

r = requests.get(url)

data = json.loads(r.text)
d = list(filter(lambda p : p['symbol'] == symbol, data))
print(d)
