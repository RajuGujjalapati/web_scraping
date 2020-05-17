# -*- coding: utf-8 -*-
"""
Created on Sun May 10 07:40:22 2020

@author: RAJU
"""
from datetime import datetime

from apiclient.discovery import build
import pandas as pd
apikey ='AIzaSyAtVPP222rPw88v4yb4NuUK67D283lYBLU'

import os

import googleapiclient.discovery

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyAtVPP222rPw88v4yb4NuUK67D283lYBLU"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.comments().list(
        part="snippet",
        textFormat="plainText",
        maxResults=10,
         id='jugPcY4Wojw',
        parentId="jugPcY4Wojw",)
        #textFormat='plainText'
    
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()