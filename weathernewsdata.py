
import re
import requests
from bs4 import BeautifulSoup

def weaternews()
    URL = 'https://weathernews.jp/onebox/tenki/tokyo/13108/'

    r = requests.get(URL)
    html = r.text.encode(r.encoding)
    s = BeautifulSoup(html, 'lxml')
    weathernow = s.find('ul', class_='weather-now__ul')
    measdata = weathernow.find_all('li')
    temp_m = re.sub("?",'',measdata[1].contents[1])
    humd_m = re.sub('%','',measdata[2].contents[1])
    pres_m = re.sub('hPa','',measdata[3].contents[1])
    
    return temp_m, humd_m, pres_m
    
