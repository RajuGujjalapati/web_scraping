from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='your api key')
#5fe0fbd068e941469a80c64805bd560#b##

# /v2/top-headlines#top_headlines
all_articles = newsapi.get_everything(q='COVID-19',
                                      sources='bbc-news,abc-news,abc-news-au,\
                                      al-jazeera-english,associated-press,axios,\
                                          ary-news,aftenposten,cnbc,cbs-news,cbc-news,\
                                              bild,cnn,the-verge' ,
                                             from_param='2020-03-11',
                                     
                                      language='en',
                                      
                                      page=1)
all_articles.keys()
all_articles['totalResults']
data_articles=all_articles['articles']
for x,y in enumerate(data_articles):
    print(f'{x}  {y["title"]}')
print(data_articles[2]['content'])
import pandas as pd
df=pd.DataFrame(all_articles)
df=pd.concat([df[['status','totalResults']],df['articles'].apply(pd.Series)],axis=1)


#print(all_articles)
# /v2/sources
sources = newsapi.get_sources()

'''
import requests
from bs4 import BeautifulSoup
url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=5fe0fbd068e941469a80c64805bd560b')
response = requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
#print(soup)
dataset= response.json()
#print(dataset)
#from pandas.io.json import json_normalize
#print(json_normalize(soup))
#res=soup.find_all('title')
#print(res)
import pandas as pd
df=pd.DataFrame(dataset)

df=pd.concat([df[['status','totalResults']],df['articles'].apply(pd.Series)],axis=1)
print(df)
df.to_csv('dataset_news.csv')
'''
