import requests
import json
import datetime

BINANCE_BASE_URL = 'https://api.binance.com'
ENDPOINT_DEPTH = '/api/v1/depth'
QS_DEPTH = 'symbol={symbol}&limit={limit}'
URL = '{base_url}{endpoint}?{query_string}'

symbol = 'TRXBTC'
limit = '20'

query_string = QS_DEPTH.format(symbol=symbol, limit=limit)

url = URL.format(base_url=BINANCE_BASE_URL,
								endpoint=ENDPOINT_DEPTH, 
								query_string=query_string)

print(f'URL: {url}')

r = requests.get(url)

#print(r.text)
data = json.loads(r.text)
print('ASK')
ask_max_quantity = 0
#ask_max_quantity_price 
for ask in data['asks']:
	if(float(ask[1]) > ask_max_quantity):
		ask_max_quantity = float(ask[1])
		ask_max_quantity_price = ask[0]
print('Price for max ask quantity ', ask_max_quantity_price)
print('BID')
bid_max_quantity = 0
#bid_max_quantity_price
for bid in data['bids']:
	if(float(bid[1]) > bid_max_quantity):
		bid_max_quantity = float(bid[1])
		bid_max_quantity_price = bid[0]
print('Price for max bid quantity ', bid_max_quantity_price)
	
