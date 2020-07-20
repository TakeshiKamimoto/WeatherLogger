#coding: utf-8

import bme280_temp
import bme280_pres
import bme280_humid
import datetime
import os
import pandas as pd
import csv
import re
import requests
from bs4 import BeautifulSoup

dir_path = '/home/pi/bme280/data'
URL = 'https://weathernews.jp/onebox/tenki/tokyo/13108/'
URL2 = 'http://web.sugiyama-u.ac.jp/~yamane/honkoma/Vantage_Pro_Plus.htm'

now = datetime.datetime.now()
filename = 'todaydata'
#label = now.strftime('%H:%M')
#date = now.strftime('%Y/%m/%d %H:%M')
time = now.strftime('%H:%M')

bme_t = bme280_temp.readData()
bme_p = bme280_pres.readData()
bme_h = bme280_humid.readData()


r = requests.get(URL)
html = r.text.encode(r.encoding)
s = BeautifulSoup(html, 'lxml')
weathernow = s.find('ul', class_='weather-now__ul')
measdata = weathernow.find_all('li')
temp_m = re.sub("?",'',measdata[1].contents[1])
humd_m = re.sub('%','',measdata[2].contents[1])
#pres_m = re.sub('hPa','',measdata[3].contents[1])

r = requests.get(URL2)
html = r.text.encode(r.encoding)
s = BeautifulSoup(html, 'lxml')
weathernow = s.find_all('tr')
pres_m = re.sub('hPa','',weathernow[5].select('small')[2].text)


if not os.path.exists('/home/pi/bme280/data'):
    os.makedirs('/home/pi/bme280/data')

f = open('/home/pi/bme280/data/'+filename+'_temp.csv','a')
f.write("'"+time+"',"+bme_t+","+temp_m+"\n")
f.close()
f = open('/home/pi/bme280/data/'+filename+'_pres.csv','a')
f.write("'"+time+"',"+bme_p+","+pres_m+"\n")
f.close()
f = open('/home/pi/bme280/data/'+filename+'_humd.csv','a')
f.write("'"+time+"',"+bme_h+","+humd_m+"\n")
f.close()

df = pd.read_csv('/home/pi/bme280/data/'+filename+'_temp.csv', header=None)
df.drop(0, inplace=True)
df.to_csv('/home/pi/bme280/data/'+filename+'_temp.csv', header=False, index=False)

df = pd.read_csv('/home/pi/bme280/data/'+filename+'_pres.csv', header=None)
df.drop(0, inplace=True)
df.to_csv('/home/pi/bme280/data/'+filename+'_pres.csv', header=False, index=False)

df = pd.read_csv('/home/pi/bme280/data/'+filename+'_humd.csv', header=None)
df.drop(0, inplace=True)
df.to_csv('/home/pi/bme280/data/'+filename+'_humd.csv', header=False, index=False)
