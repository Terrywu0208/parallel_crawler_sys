import typing
from datetime import datetime
from worker import app
import crawler_pk.udn_news_crawler as nc
import crawler_pk.weather_crawler as wc
# from db import db as db_s
# from db import router as db_router
from db_upload import uplaod


# 註冊 task, 有註冊的 task 才可以變成任務發送給 rabbitmq
@app.task()
def crawler(dataset: str,parameters: typing.Dict[str, str],):
    time_format = datetime.strptime(parameters['crawler_date'],"%Y-%m-%d")
    if dataset == "udn_news_crawler":
        df = nc.news_crawler(time_format)
        table_name= "udn_data"
    elif dataset == "weather_crawler":
        df = wc.weather_crawler(time_format)
        table_name= "weather_data"
    # db_s.upload_data(df, dataset, db_router.Router.mysql_financialdata_conn)
    uplaod.data_upload(df, table_name= table_name)
    print("crawler_date : ",parameters['crawler_date'])
    print(df)
    print("crawler")
    print("upload db")


