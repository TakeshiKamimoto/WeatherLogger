#coding: utf-8

import bme280_sample
import weathernewsdata
import webpressdata
import datetime
import os
import pandas as pd
import csv
import re
import requests
from bs4 import BeautifulSoup

dir_path = '/home/pi/bme280/data'

now = datetime.datetime.now()
filename = 'todaydata'
#label = now.strftime('%H:%M')
#date = now.strftime('%Y/%m/%d %H:%M')
time = now.strftime('%H:%M')

sensdata = bme280_sample.readData()
bme_t = sensdata[0]
bme_p = sensdata[1]
bme_h = sensdata[2]

webdata = weathernewsdata.readData()
temp_m = webdata[0]
humd_m = webdata[1]

pres_m = webpressdata.readData()

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
