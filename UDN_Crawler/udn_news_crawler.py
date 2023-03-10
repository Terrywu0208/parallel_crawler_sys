import requests
from bs4 import BeautifulSoup
import json 
import pandas as pd
from datetime import datetime, timedelta
import time
import re

def news_crawler(start_time):
    news_list_all = []
    page = 1
    while page <2:
        response = requests.get(f"https://udn.com/api/more?page={page}&date={start_time}&type=archive")
        json_response = json.loads(response.text)

        try:
            news_list = json_response["lists"]
        except:
            break

        news_list_all.extend(json_response["lists"])
        page+=1

        time.sleep(3)
    return news_list_all

def change_date(search_time):
    post_time = datetime.strptime(d['date'], "%Y-%m-%d %H:%M")
    post_time = post_time.strftime("%Y%m%d%H%M")
    return post_time

def clean_data(search_result):
    df = pd.DataFrame(search_result)
    df = df.drop(["titleLink","cateLink"], axis=1)
    df["time"] = df["time"].apply(change_date)
    return df

if __name__ == "__main__":
    start_t = datetime(2022,2,5)
    start_time = start_t.strftime("%Y%m%d")
    search_result = news_crawler(start_time)
    final_result = clean_data(search_result)
    final_result.to_csv("result.csv")

