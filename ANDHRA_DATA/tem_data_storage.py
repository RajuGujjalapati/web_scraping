from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import openpyxl
from openpyxl import Workbook
#########Requested to give proper 'Chrome-driver path' as per your system##################
driver = webdriver.Chrome()
driver.get('http://registration.ap.gov.in/UnitRateMV.do?method=getDistrictList&uType=P')


##########As per the requirement going through one value#####################################
##########default district value if need we can automate this too##################################

select_district = Select(driver.find_element_by_id('districtCode'))
select_district.select_by_value('10')

#paramss={'method': 'getDistrictList','uType': 'P'}
#head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',"X-Requested-With": "XMLHttpRequest"}
req=requests.get('http://registration.ap.gov.in/UnitRateMV.do?method=getMandalListByDistCode&districtCode=10')#params=paramss, headers = head
#print(req)
time.sleep(1)
soup = BeautifulSoup(req.text, 'lxml')  
res2=soup.find('mandalCode')
final=soup.find('p')
#print('final......',final)
end=final.text.split('#')
#print('enddddddddd:',end)#
a=end
b=' '.join(a)
c=b.replace(' ','')
print(str(c))
mandal_codes=re.findall('\d+',c)
mandal_names=re.findall("[a-zA-Z.@()]+",c)
print(mandal_names)
print(mandal_codes)
final_mandal_dict=dict(zip(mandal_codes,mandal_names))
print(final_mandal_dict)

'''

dinchaka=[]
for ele in end:
    dik=re.findall('[0-9]',ele)
    dinchaka.extend(dik)
print("dinchaka",dinchaka)#
final_str=''
for i in dinchaka:
    final_str+=i
#print(final_str)
n=2
mandal_values=[final_str[i:i+n] for i in range(0, len(final_str), n)]
print("manda_codes",mandal_values)
#############end of list of values#########
'''
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
    '''
    village_values=re.findall('\d+',koi)
    village_str=re.findall('\w+',koi)
    print("village str values",village_str)
    filterd_val=[]
    for val in village_str:
        if val.isdigit():
            pass
        else:
            filterd_val.append(val)
    final_filter=filterd_val[1:]
    print('filterd_val are:', filterd_val[1:])
    '''
    final_village_dict=dict(zip(village_codes,village_names))
    print(final_village_dict)


    
    for code,name in final_village_dict.items():
        
        select_village = Select(driver.find_element_by_id('villageCode'))
        select_village.select_by_value(str(code))#major error point
        for i in range(201,202):
            #time.sleep(1)
           
            print("survey No:",i, "for village",name)
            driver.find_element_by_xpath("//*[@id='surveyNo']").send_keys(i)
            driver.find_element_by_xpath("//*[@id='Table8']/tbody/tr/td/form/center/input").click()
            time.sleep(2)
            table=(driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td/center[2]/table[1]"))
            table_text=table.text[83:]+' '+name+' '+mandal_values
            print(table_text)
            with open ('data.txt','a') as f:
                f.write(table_text)
                f.write('\n')
                
            driver.execute_script("window.history.go(-1)")
            driver.refresh()
            time.sleep(2)
            
            select_district = Select(driver.find_element_by_id('districtCode'))
            select_district.select_by_value('10')
            time.sleep(2)#
            try:                
                select_mandal = Select(driver.find_element_by_id('mandalCode'))
                select_mandal.select_by_value(str(mandal_codes))
                
            except Exception as e:
                print("exception is:",e)
                continue
                '''
                driver.refresh()
                select_district = Select(driver.find_element_by_id('districtCode'))
                select_district.select_by_value('10')
                select_mandal = Select(driver.find_element_by_id('mandalCode'))
                select_mandal.select_by_value(str(mandal_codes))
                '''
            except  NoSuchElementException:
                continue
                '''
                driver.refresh()
                select_district = Select(driver.find_element_by_id('districtCode'))
                select_district.select_by_value('10')
                select_mandal = Select(driver.find_element_by_id('mandalCode'))
                select_mandal.select_by_value(str(mandal_codes))
                '''
                
               
            try:
                time.sleep(2)
                select_village = Select(driver.find_element_by_id('villageCode'))
                select_village.select_by_value(str(code))
            except Exception as e:
                continue
                '''
                driver.refresh()
                select_district = Select(driver.find_element_by_id('districtCode'))
                select_district.select_by_value('10')
                select_mandal = Select(driver.find_element_by_id('mandalCode'))
                select_mandal.select_by_value(str(mandal_codes))
                select_village = Select(driver.find_element_by_id('villageCode'))
                select_village.select_by_value(str(code))
                '''
            except  NoSuchElementException:
                continue
                '''
                driver.refresh()
                select_district = Select(driver.find_element_by_id('districtCode'))
                select_district.select_by_value('10')
                select_mandal = Select(driver.find_element_by_id('mandalCode'))
                select_mandal.select_by_value(str(mandal_codes))
                select_village = Select(driver.find_element_by_id('villageCode'))
                select_village.select_by_value(str(code))
                '''
            except Exception as e:
                print("exception is:",e)
                continue
                '''
                driver.refresh()
                select_district = Select(driver.find_element_by_id('districtCode'))
                select_district.select_by_value('10')
                select_mandal = Select(driver.find_element_by_id('mandalCode'))
                select_mandal.select_by_value(str(mandal_codes))
                select_village = Select(driver.find_element_by_id('villageCode'))
                select_village.select_by_value(str(code))
                '''
                
                
                 

'''
                
                #driver.execute_script("window.history.go(-1)")
                driver.refresh()
                time.sleep(3)
                
                select_district = Select(driver.find_element_by_id('districtCode'))
                select_district.select_by_value('10')
                select_mandal = Select(driver.find_element_by_id('mandalCode'))
                select_mandal.select_by_value(str(mandal_codes))
                time.sleep(1)
                select_village = Select(driver.find_element_by_id('villageCode'))
                select_village.select_by_value(str(value))

            df=pd.read_csv('data.txt',header=None, delimiter=' ')
            df = df[df.S.No.str.contains('S.No') == False]
            df.to_csv('df_final.csv')
driver.stop_client()
driver.close()


    

    

    
    
                
            




        
            
            
                



"""       

                lis=[]
                with open ('data.txt','r') as lis:
                    data = lis.readlines()
                    fi=data[2:]
                    
                    #lis.append(fi)
                    final_str=(''.join(map(str,fi)))
                    while final_str!='':
                        lis.append(final_str)
                        print(lis)
                    with open ('final.txt', 'a') as final:
                        final_data = final.write(final_str)
                        final.write('\n')
                    
                    
            with open('final.txt','a') as data:
                data.write(final_data)
                data.write('\n')
                
                
            
            lin=[]
            for line in lines:
                if line.startswith('S'):
                    del line
                else:
                    lin.append(line)
            
            print(lin)
            str1=' '
            with open ('final.ttxt','a') as r:

                a=str1.join(lin)
                #f.write('\n')
            print(str1)2221
              
            df=pd.read_csv('data.txt',delimiter=' ',header=None)
            print(df)
            li.append(df[1:])
            frame = pd.concat(li,axis=0,ignore_index=True)
            frame.to_csv('final_data.csv')
            
'''
          


