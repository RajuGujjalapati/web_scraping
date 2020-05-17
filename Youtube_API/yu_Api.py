#pip install google-api-python-client
#python cilent which helps to fetch the details from youtube
apikey ='AIzaSyAtVPP222rPw88v4yb4NuUK67D283lYBLU'

from apiclient.discovery import build
import pandas as pd
'''
youtube = build('youtube','v3',developerKey=apikey)
print((youtube))
#youtube is a resource object now which helps to fetch details from youtube_api
req=youtube.search().list(q='python', part='snippet',type='video', maxResults=50)#q-quiery:search result, type(of content)-playlist,channel
########################
 By default we get 5 values we can increase this count using maxResults=50
max will be 50
res=req.execute()
find=res['items']
print(find)
find1=res['items'][0]['snippet']
#########or#################
for i in find:
    print(i['snippet']['channelTitle'])
print(find1)
a=res['items']
df=pd.DataFrame(a)
print(df)
df.to_csv('read.csv')
'''
##############################################################################################################################################################
#####fetching videos from one year to another year#############################
from datetime import datetime
youtube = build('youtube','v3',developerKey=apikey)
print((youtube))
start_time = datetime(year=2015, month=1, day=1).strftime('%Y-%m-%dT%H:%M:%SZ')
end_time = datetime(year=2016, month=1, day=1).strftime('%Y-%m-%dT%H:%M:%SZ')


#youtube is a resource object now which helps to fetch details from youtube_api
req=youtube.search().list(q='python', part='snippet',type='video',
                          maxResults=10,publishedAfter=start_time,publishedBefore=end_time).execute()
print(req)

for items in req['items']:
    print(items['snippet']['title'],items['snippet']['publishedAt'], items['id']['videoId'])
