from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
#########Requested to give proper 'Chrome-driver path' as per your system##################
driver = webdriver.Chrome()
driver.get('http://registration.ap.gov.in/UnitRateMV.do?method=getDistrictList&uType=P')


##########As per the requirement going through one value#####################################
##########default district value if need we can automate this too##################################
driver.implicitly_wait(10)
#code (HTML) runs on background for 10 seconds again and again to fetch the element.
with open('data.txt','w') as f:
    pass
select_district = Select(driver.find_element_by_id('districtCode'))
select_district.select_by_value('10')


req=requests.get('http://registration.ap.gov.in/UnitRateMV.do?method=getMandalListByDistCode&districtCode=10')
#print(req)
time.sleep(1)
soup = BeautifulSoup(req.text, 'lxml')  
res2=soup.find('mandalCode')
final=soup.find('p')
#print('final......',final)
end=final.text.split('#')
a=end
b=' '.join(a)
c=b.replace(' ','')
print(str(c))
mandal_codes=re.findall('\d+',c)
mandal_names=re.findall("[a-zA-Z.@()]+",c)
print(mandal_names)
print(mandal_codes)
final_mandal_dict=dict(zip(mandal_codes,mandal_names))
#print(final_mandal_dict)

array_val=['53','50','54','26']
array_str=['THAVANAMPALLE','PENUMURU','CHITTOOR','TIRUPATIRURAL']
final_mandal_dict=dict(zip(array_val,array_str))
print(final_mandal_dict)
for mandal_codes,mandal_values in final_mandal_dict.items():

    select_mandal = Select(driver.find_element_by_id('mandalCode'))
    select_mandal.select_by_value(str(mandal_codes))
    req1=requests.get('http://registration.ap.gov.in/UnitRateMV.do?method=getVillageList&districtCode=10&mandalCode='+mandal_codes+'&sType=R')#, params=paramss, headers = head)
    print(req1)
    soup = BeautifulSoup(req1.text, 'lxml')  
    res2=soup.find('villageCode')
    print(res2)
    final=soup.find('p')
    print(final.text)
    koi=final.text
    a1=koi
    b1=' '.join(a1)
    c1=b1.replace(' ','')
    print(str(c1))
    village_codes=re.findall('\d+',c1)
    village_codes=[data for data in village_codes if len(data)>=4]
    
    village_names=re.findall("[a-zA-Z.@()]+",c1)
    print(village_names)
    print(village_codes)
    #####
  
    final_village_dict=dict(zip(village_codes,village_names))
    print(final_village_dict)


    
    for code,name in final_village_dict.items():
        driver.implicitly_wait(5)                
        select_village = Select(driver.find_element_by_id('villageCode'))
        select_village.select_by_value(str(code))#major error point
        for i in range(1,100):
            #time.sleep(1)
           
            print("survey No:",i, "for village",name)
            driver.find_element_by_xpath("//*[@id='surveyNo']").send_keys(i)
            driver.find_element_by_xpath("//*[@id='Table8']/tbody/tr/td/form/center/input").click()
            time.sleep(2)
            table=(driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td/center[2]/table[1]"))
            table_text=table.text[83:]#+' '+name+' '+mandal_values
            x=table_text.split('  ')
            print(x)
            x_=''.join(x)
            #x1=x_.replace('\n',',')
            #print('x1 is:',x1)
            x2=x_.split('\n')
            y=[mandal_values+' '+name+' '+u  for u in x2 if len(u)>=30]
            
            y1='\n'.join(y)
                             
            print("finalDataIntoFile",y1)
            with open ('data.txt','a') as f:
                f.writelines(y1)
                f.write('\n')
            headers=['MANDAL','VILLAGE','S.NO','SURVEY NO.','EXTENT (UNIT)','NOTIFICATION NUMBER','NOTIFICATION DATE','E','OTHER', 'REFERENCE']
            df=pd.read_csv('data.txt',delimiter=' ',names=headers)
            df['SURVEY NO.'] = "'"+df['SURVEY NO.']
            print(df)
            df['NOTIFICATION DATE'] = df['NOTIFICATION DATE'] +' '+"'"+df['E']
            print('#########################',df)
            df=df.drop('E',1)
            print(df)
            df['OTHER REFERENCE'] = df['OTHER'] +' '+ df['REFERENCE']
            df =df.drop(['OTHER','REFERENCE'],1)
            df.to_csv('fianldata.csv')
            driver.execute_script("window.history.go(-1)")
            driver.refresh()
            time.sleep(3)
            
            select_district = Select(driver.find_element_by_id('districtCode'))
            select_district.select_by_value('10')
            time.sleep(2)#
            try:                
                select_mandal = Select(driver.find_element_by_id('mandalCode'))
                select_mandal.select_by_value(str(mandal_codes))
                
            except Exception as e:
                print("exception is:",e,' at ',mandal_values)
                continue
                
               
            try:
                time.sleep(1)
                select_village = Select(driver.find_element_by_id('villageCode'))
                select_village.select_by_value(str(code))
            except  NoSuchElementException:
                continue
            except Exception as e:
                print("exception is:",e,' at ',name)
                continue
            
                
           
                
                
                 
    

    

    
    
                
            




        
            
            
                



 


