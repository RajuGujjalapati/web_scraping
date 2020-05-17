# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 09:48:24 2020

@author: RAJU
"""


import requests
r=requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
#first 500 lines from html
print(r.text[0:500])
from bs4 import BeautifulSoup
soup=BeautifulSoup(r.text,'html.parser')
results = soup.find_all('span', attrs={'class':'short-desc'})
len(results)
results[0:3]
results[-1]
