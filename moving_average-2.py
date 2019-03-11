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

size = 10
counter = 0
moving_total = 0.0
window = [0.0] * size
items = []
data = json.loads(r.text)

for kline in data[:size]:
	counter += 1
	value = float(kline[4])
	moving_total -= window[0]
	window.pop(0)
	moving_total += value
	window.append(value)
	ma = moving_total/(counter)
	item = {"date":kline[6], "price": value, "moving_average":ma}
	items.append(item)

for kline in data[size:]:
	value = float(kline[4])
	moving_total -= window[0]
	window.pop(0)
	moving_total += value
	window.append(value)
	ma = moving_total/size
	item = {"date":kline[6], "price": value, "moving_average":ma}
	items.append(item)
print(items)
 
		

