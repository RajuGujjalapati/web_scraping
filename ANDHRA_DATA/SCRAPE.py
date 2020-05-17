# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:33:25 2020

@author: RAJU
"""
from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
#from requests_html import html

req=requests.get('http://registration.ap.gov.in/UnitRateMV.do?method=getDistrictList&uType=P')
soup = BeautifulSoup(req.text, 'lxml')
# # print(soup)
# #headline=match.find('h2').text
# # res=soup.find('.formbg2 option')
res=soup.find_all('td',{'class':'formbg2'})
res_try=soup.find('td.formbg2')
#print(res_try)
# for match in res:
#     #print(match.find_all('option'))
#     for i in match.find_all('option'):
#         print(i)
#         if i=='<option value="10">CHITOOR</option>':
#             print(i)
        
    
#res1=res.find('option',first=True)
# print(res)

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
driver.get('http://registration.ap.gov.in/UnitRateMV.do?method=getDistrictList&uType=P')

select_district = Select(driver.find_element_by_id('districtCode'))

# select by visible text
#select.select_by_visible_text('CHITTOR')

#select by value 
select_district.select_by_value('10')
time.sleep(2)
select_mandal = Select(driver.find_element_by_id('mandalCode'))
select_mandal.select_by_value('10')
#to extract the mandal id , we dont know the id's , so try to get mandal id's.
# for i in range(1,80):
#     try:
#         pass
#         #print("value is",select_mandal.select_by_value(str(i)),i)
#     except Exception as e:
#         #print(select_mandal.select_by_value(str(i)))
#         continue
soup = BeautifulSoup(req.text, 'lxml')  
res2=soup.find('villageCode')
print(res2)
time.sleep(2)
select_village = Select(driver.find_element_by_id('villageCode'))
select_village.select_by_value('1010004')
print((select_village))
for j in range(1,100):
    try:
        print("value is",select_village.select_by_value('517194'),j)
    except Exception as e:
        continue
print("OK")