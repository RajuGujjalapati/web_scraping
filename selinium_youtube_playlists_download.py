from selenium import webdriver
import time
import os
import requests
from bs4 import BeautifulSoup
req=requests.get('https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH')
soup = BeautifulSoup(req.text, 'lxml')
#print(soup)
result =soup.find_all('a', {'class':'pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link'})
#print(result)
os.remove('all_links.txt')
for i in  range(len(result)):
    try1=result[i]['href']
    try2=try1.replace('amp;','')
    with open('all_links.txt','a') as f:
        f.write('https://www.youtube.com')
        f.write(try2)
        f.write('\n')
data=open('all_links.txt','r')
lines=data.readlines()

for line in lines:
    print(line)
    driver =webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
    driver.get("https://en.savefrom.net/1-youtube-video-downloader-1/")
    driver.find_element_by_id("sf_url").send_keys(line)
    time.sleep(4)
    driver.find_element_by_id("sf_submit").click()
    time.sleep(10)
    driver.find_element_by_id("sf_result").click()
    time.sleep(5)

'''       
#result2 = soup.find_all('a')#wc-endpoint
#print(result2)

how to download youtube videos to system

driver =webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
driver.get("https://www.youtube.com/playlist?list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t")
for i in range(1,26):

    driver.find_element_by_id("sf_url").send_keys("https://www.youtube.com/watch?v=QksUFT2Cmlo&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t&index={}".format(i))
#time.sleep(1)
    driver.find_element_by_id("sf_submit").click()
    time.sleep(3)
#a=[];
#a=driver.find_element_by_class_name('link link-download subname ga_track_events download-icon').click()
#alert_obj = driver.switch_to.alert
#alert_obj.dismiss()
    title = driver.find_element_by_id("sf_result").click()
    time.sleep(10)
#title.click()
#//*[@id="j_analyse_container"]/main/div[1]/div/div[2]/div/div[2]/div[1]/a
#/html/body/div[3]/main/div[1]/div/div[2]/div/div[2]/div[1]/a/i
#//*[@id="sf_result"]/div/div[1]/div[2]/div[2]/div[1]/a
/watch?v=wYJAtx4HL6U&amp;list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t&amp;index=3&amp;t=0s">
watch?v=wYJAtx4HL6U&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t&index=3&t=0s
'''
