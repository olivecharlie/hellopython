import requests
import hmac
import hashlib
import time
import json

with open('_config.json', 'r') as f:
	config = json.load(f)

secret = config['DEFAULT']['SECRET_KEY']
key = config['DEFAULT']['API_KEY']

BINANCE_BASE_URL = 'https://api.binance.com'
HEADER_API_KEY = 'X-MBX-APIKEY'
ENDPOINT_ALL_ORDERS = '/api/v3/allOrders'
QS_ALL_ORDERS = 'symbol={symbol}&timestamp={timestamp}'
URL = '{base_url}{endpoint}?{query_string}&signature={signature}'

#container for any headers. As a minimum, the API key from Binance must be passed in the header.
headers = {
	HEADER_API_KEY : key
	}

print(headers)

symbol = 'TRXBTC'

#Timestamp in miliseconds is required parameter to all calls.
ts = int(time.time() * 1000)
#print(f'Timestamp: {ts}')

#the query string is hashed using into a HMAC (hashed message authentication code) using the SHA256 hash
#function. This is a symmetric authentication and data integrity mechanism.
query_string = QS_ALL_ORDERS.format(symbol=symbol, timestamp=ts)
signature  = hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
#print(f'Signature: {signature}')

url = URL.format(base_url=BINANCE_BASE_URL,
								endpoint=ENDPOINT_ALL_ORDERS, 
								query_string=query_string, 
								signature=signature)

print(f'URL: {url}')

r = requests.get(url, headers=headers)
#print(r.json())
#print(r.text)

resp_obj = r.json() #json.loads(r.text)
for r in resp_obj:
		if r['status'] == 'FILLED':
			print('ORDER:')
			for i in r:
				print(f'	{i} : {r[i]}')

