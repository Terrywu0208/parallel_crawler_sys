import importlib
import typing
from datetime import datetime
from worker import app
import crawler_pk.udn_news_crawler as nc

# 註冊 task, 有註冊的 task 才可以變成任務發送給 rabbitmq
@app.task()
def crawler(dataset: str,parameters: typing.Dict[str, str],):
    # 使用 getattr, importlib,
    # 根據不同 dataset, 使用相對應的 crawler 收集資料
    # 爬蟲
    # df = getattr(importlib.import_module(f"crawler.{dataset}"),"crawler",)(parameters=parameters)
    # df = getattr(importlib.import_module(f"crawler.{dataset}"))(parameters=parameters)
    # print(df)
    time_format = datetime.strptime(parameters['crawler_date'],"%Y-%m-%d")
    df_nc = nc.news_crawler(time_format)
    print("'crawler_date : ",parameters['crawler_date'])
    print(df_nc)
    print("crawler")
    print("upload db")
