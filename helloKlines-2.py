import requests
import json
import datetime

BINANCE_BASE_URL = 'https://api.binance.com'
ENDPOINT_KLINES = '/api/v1/klines'
QS_KLINES = 'symbol={symbol}&interval={interval}'
URL = '{base_url}{endpoint}?{query_string}'

symbol = 'TRXBTC'
interval = '1h'

query_string = QS_KLINES.format(symbol=symbol, interval=interval)

url = URL.format(base_url=BINANCE_BASE_URL,
								endpoint=ENDPOINT_KLINES, 
								query_string=query_string)

print(f'URL: {url}')

r = requests.get(url)

#print(r.text)
data = json.loads(r.text)
for kline in data:
		print('KLINE')
		print(' open_time', datetime.datetime.fromtimestamp(int(kline[0])/1000))
		print(' open', kline[1])
		print(' high', kline[2])
		print(' low', kline[3])
		print(' close', kline[4])
		print(' volume', kline[5])
		print(' close_time', datetime.datetime.fromtimestamp(int(kline[6])/1000))
		print(' quote_asset_volume', kline[7])
		print(' number', kline[8])
		print(' taker_base_vol', kline[9])
		print(' taker_quote_vol', kline[10])
		print(' ignore', kline[11])
