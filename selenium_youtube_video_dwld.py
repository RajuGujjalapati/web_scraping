from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
req=requests.get('https://www.youtube.com/playlist?list=PLS1QulWo1RIZ77GWt3rQUggB7vm46ylYO')
soup = BeautifulSoup(req.text, 'lxml')
#print(soup)
result =soup.find_all('a', {'class':'pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link'})
#print(result)
for i in  range(len(result)):
    try1=result[i]['href']
    try2=try1.replace('amp;','')
    with open('all_links.txt','a') as f:
        f.write('https://www.youtube.com')
        f.write(try2)
        f.write('\n')
print("completed")
