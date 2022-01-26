#pip install binance
#pip install songline
from binance import Client
from songline import Sendline
api_key ='----Your-api-key-------- '
api_secret = '-----Your-api-secret---------'
client = Client(api_key, api_secret)

token = '---------Your--Token-------'
messenger = Sendline(token)

#depth = client.get_order_book(symbol='BTCBUSD')
#print(depth)

prices = client.get_all_tickers()
mycoin = ['BTCBUSD']
for p in prices:
    for c in mycoin:
        sym = c
        if p['symbol'] == sym:
             pc = float(p['price'])
             rate = 33.13
             cal = pc*rate
             print('เหรียญ: {} ราคา: {:,.5f} บาท'.format(sym,cal))
             print('ราคา USD: {}'.format(pc))
alltext = ''
for c in mycoin:
    text = 'BTC/THB  ราคาปัจจุบัน {} '.format(cal)
    alltext = alltext + text
messenger.sendtext(alltext)
          
           

