from worker import app
import pk.udn_news_crawler as uc
import pk.weather_crawler as wc
from datetime import datetime

# 註冊 task, 有註冊的 task 才可以變成任務發送給 rabbitmq
@app.task()
def crawler(x):
    print("crawler")
    uc_result = uc.news_crawler(datetime(2022,2,5))
    wc_result = wc.weather_crawler(datetime(2023,3,19))
    print(uc_result)
    print(wc_result)
    print("upload db")
    return x
