from songline import Sendline
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from binance import Client

token = '------Your Token--------' #generate token for send line
messenger = Sendline(token)
#-------------------------------------------------------------Aqi----------------------------------------------------
def Airq(ID):
    url = 'https://www.iqair.com/th-en/thailand/{}'.format(ID)

    webopen = req(url)
    page_html = webopen.read()
    webopen.close() 

    data = soup(page_html,'html.parser')
    # print(data)
    airq = data.find_all('p',{'class':'aqi-value__value'})
    airq = airq[0].text
    #print(airq)

    province = data.find_all('h1',{'class':'pagetitle__title'})
    province = province[0].text.strip()
    print(province, airq)
    return(province, airq)

allid = ['sukhothai']
alltext = ''

for d in allid:
    pv = Airq(d)
    text1 = '{} {}'.format(pv[0],pv[1])
    alltext1 = alltext + text1 + '\n'

#----------------------------------------------------BTC-------------------------------------------------------
    
api_key ='------------------Your--api--key------------------------ '
api_secret = '-------Your--api--secret-----------------------------'
client = Client(api_key, api_secret)

prices = client.get_all_tickers()
mycoin = ['BTCBUSD']
for p in prices:
    for c in mycoin:
        sym = c
        if p['symbol'] == sym:
             #print(p)
             pc = float(p['price'])
             rate = 33.13
             cal = pc*rate
             print('เหรียญ: {} ราคา: {:,.5f} บาท'.format(sym,cal))
             print('ราคา USD: {}'.format(pc))

for c in mycoin:
    text = 'BTC/USD Price: {:,.8f} '.format(pc)
    alltext = alltext1+ alltext + text + '\n'

#----------------------------------------------------Pig Price--------------------------------------------------------------

url = 'https://www.kasetprice.com/%E0%B8%A3%E0%B8%B2%E0%B8%84%E0%B8%B2/%E0%B9%80%E0%B8%99%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%A1%E0%B8%B9/%E0%B8%A7%E0%B8%B1%E0%B8%99%E0%B8%99%E0%B8%B5%E0%B9%89'

webopen = req(url)
page_html = webopen.read()
webopen.close()

data = soup(page_html,'html.parser')
Pig = data.find_all('div',{'class':'price-list-cost'})
Pig = Pig[-1].text.strip()

print(Pig)
pigprice = ['Pig']
alltext = ''
for p in pigprice:
    pp = Pig
    text2 = 'ราคาเนื้อหมูวันนี้ : {} บาท'.format(pp)
    alltext ='\n' + alltext1 + alltext + text + text2 + '\n'
messenger.sendtext(alltext)





          


