import requests
from bs4 import BeautifulSoup
import json 
import pandas as pd
from datetime import datetime, timedelta
import time
import re

def change_date(df):
    post_time = datetime.strptime(df['date'], "%Y-%m-%d %H:%M")
    post_time = post_time.strftime("%Y%m%d%H%M")
    return post_time

def clean_data(search_result):
    df = pd.DataFrame(search_result)
    df = df.drop(["titleLink","cateLink"], axis=1)
    df["time"] = df["time"].apply(change_date)
    return df

def news_crawler(start_date):
    start_date = start_date.strftime("%Y%m%d")
    news_list_all = []
    page = 1
    while page <2:
        response = requests.get(f"https://udn.com/api/more?page={page}&date={start_date}&type=archive")
        json_response = json.loads(response.text)

        try:
            news_list = json_response["lists"]
        except:
            break

        news_list_all.extend(json_response["lists"])
        page+=1

        time.sleep(3)
    final_result = clean_data(news_list_all)
    return final_result

if __name__ == "__main__":
    search_result = news_crawler(datetime(2022,2,5))