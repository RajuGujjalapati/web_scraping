from bs4 import BeautifulSoup
import requests
from parse import *

r=requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
#print(res.text[0:1500])

#coverpage = r.content
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('span',{'class':"short-desc"})
'''   OR   ''''
#soup('span',attrs={'class': 'sadssd'})
#soup('span',class_='asdasada')
print(len(results))
print(results[1:4])
first_res=results[0]
#just raking one reocrd
first_result=first_res.find('strong').text[0]
''' OR '''
#we can just specify --> first_res.strong  ,just  when we accesing only one attri   
print(first_res)
print(first_res.contents)#it gives a list
print(first_res.contents[1])
attr_res=first_res.find('a').text
#text:extracts the tag and returns a string
#contents: extracts the children of the tag and returns the list.
#find: searches for the first matvhing of the tag, and return Tag.
#find_all:searches for the all matching of the tags and ResultSet object
print(attr_res[1:-1])
attr_href=first_res.find('a')['href']
print(attr_href)



records=[]

for result in results:
    date=result.find('strong').text[0:-1]+', 2017'
    lie=result.contents[1][1:-2]
    explaination = result.find('a').text[1:-1]
    url=result.find('a')['href']
    records.append((date,lie,explaination,url))
print(records[0:3])
import pandas as pd
df=pd.DataFrame(records,columns=['date','lie','explaination','url'])
df['date']=pd.to_datetime(df['date'])
df.to_csv('trump_lies.csv', index=False, encoding='utf-8')
    
#all_trending= news_box.find_all('a')
#for news in all_trending:
 #   print(news.text)
#import os
#list_dir=os.listdir(r'C:\Users\New\OneDrive\Desktop\MACHINE LEARNING\PANDAS\web-scraping\bbc-fulltext\bbc')
#print(list_dir)
import glob
#q=glob.glob(r'C:\Users\New\OneDrive\Desktop\MACHINE LEARNING\PANDAS\web-scraping\bbc-fulltext\bbc\business\0**.txt')



