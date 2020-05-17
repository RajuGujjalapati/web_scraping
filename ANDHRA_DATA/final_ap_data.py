from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import openpyxl
from openpyxl import Workbook

driver = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
driver.get('http://registration.ap.gov.in/UnitRateMV.do?method=getDistrictList&uType=P')

select_district = Select(driver.find_element_by_id('districtCode'))
select_district.select_by_value('10')
time.sleep(2)



paramss={'method': 'getDistrictList','uType': 'P'}
head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',"X-Requested-With": "XMLHttpRequest"}
req=requests.get('http://registration.ap.gov.in/UnitRateMV.do?method=getMandalListByDistCode&districtCode=10', params=paramss, headers = head)
print(req)



soup = BeautifulSoup(req.text, 'lxml')  
res2=soup.find('villageCode')
final=soup.find('p')
end=final.text.split('#')

dinchaka=[]
for ele in end:
    dik=re.findall('[0-9]',ele)
    dinchaka.extend(dik)
print(dinchaka)
final_str=''
for i in dinchaka:
    final_str+=i
print(final_str)
n=2
mandal_values=[final_str[i:i+n] for i in range(0, len(final_str), n)]
print("looking for dead end",mandal_values)
#############end of list of values#########
for values in mandal_values:
    select_mandal = Select(driver.find_element_by_id('mandalCode'))
    select_mandal.select_by_value(str(values))
    

    req1=requests.get('http://registration.ap.gov.in/UnitRateMV.do?method=getVillageList&districtCode=10&mandalCode={}&sType=R'.format(int(value)), params=paramss, headers = head)
    soup = BeautifulSoup(req1.text, 'lxml')  
    res2=soup.find('villageCode')
    final=soup.find('p')
    print(type(final.text))
    koi=final.text
    last=re.findall('\d+',koi)
    print(last)###########end of list of values########
    select_village = Select(driver.find_element_by_id('villageCode'))
    select_village.select_by_value(str(last))
    driver.find_element_by_xpath("//*[@id='surveyNo']").send_keys(250)

driver.find_element_by_xpath("//*[@id='Table8']/tbody/tr/td/form/center/input").click()
table=(driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td/center[2]/table[1]"))
table_text=(table.text)
print(table_text,end="")
with open ('data.txt','w') as f:
    f.write(table_text)
df=pd.read_csv('data.txt',delimiter=' ')
print(df)
df.to_csv('final_data.csv')
data=open('data.txt','r')
conver_list=data.readlines()
"""
def func():
    for i in conver_list:
        split=i.split(' ')
        yield split
da=func()
for j in da:
    with open('data.txt','w') as f:
        f.append(j)
    


#req2=requests.get('http://registration.ap.gov.in/UnitRateMV.do')
#soup=BeautifulSoup(req.text,'lxml')
#print(soup.find('tbody'))

#//*[@id="Table8"]
pandas_data=w.row_data(1)[1]
pa=pandas_data.split(' ')
print(pa)
dataframe=pd.DataFrame(pa[25:36])
df_final=dataframe.T
df_final.to_csv("andhra_data.csv")
table link/ https://chercher.tech/python/table-selenium-python /

"""
"""
while "" in end:
    end.remove("")
#print("modified:",str(end))
final_string=""
for i in end:
    final_string+=i+','
#print(final_string)
end_final=final_string.split('/')
#print(end_final)
#res = list(map(lambda sub:int(str((''.join([ele for ele in sub if ele.isnumeric()])))), end_final))
#print(res)
#dikku=re.findall('[0-9]',end)
#print(dikku)"""


