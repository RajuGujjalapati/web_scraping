import os, urllib
import requests
BASE_DIR=r'C:\Users\New\OneDrive\Desktop\MACHINE LEARNING\web-scraping'
output_file = os.path.join(BASE_DIR,'drinks.csv')
drinks_data=urllib.Request.urlretrieve('https://github.com/justmarkham/pandas-videos/blob/master/data/drinks.csv',output_file)
print(output_file)
