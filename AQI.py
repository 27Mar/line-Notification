#pip install BeautifulSoup4 
#pip install songline
from songline import Sendline
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req

token = '-------Your-Token----------'
messenger = Sendline(token)
#messenger.sendtext()
#messenger.sticker(103,1,'Hi')
#url =''
#messenger.sendimage(url)

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
    text = ' {} {}'.format(pv[0],pv[1])
    alltext = alltext + text + '\n'
messenger.sendtext(alltext)

