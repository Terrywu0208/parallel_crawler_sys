import importlib
import typing
from datetime import datetime
from worker import app
import crawler_pk.udn_news_crawler as nc
import crawler_pk.weather_crawler as wc
import db


# 註冊 task, 有註冊的 task 才可以變成任務發送給 rabbitmq
@app.task()
def crawler(dataset: str,parameters: typing.Dict[str, str],):
    time_format = datetime.strptime(parameters['crawler_date'],"%Y-%m-%d")
    if dataset == "udn_news_crawler":
        df = nc.news_crawler(time_format)
    elif dataset == "weather_crawler":
        df = wc.weather_crawler(time_format)
    db.db.upload_data(df, dataset, db.router.mysql_financialdata_conn)
    print("crawler_date : ",parameters['crawler_date'])
    print(df)
    print("crawler")
    print("upload db")
