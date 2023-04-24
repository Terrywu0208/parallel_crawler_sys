from worker import app
import pk.udn_news_crawler as uc
import pk.weather_crawler as wc
import pk.ppt_crawler as pc
from datetime import datetime

# 註冊 task, 有註冊的 task 才可以變成任務發送給 rabbitmq
@app.task()
def crawler(x):
    print("---------------- start crawler ------------------")
    start_date_str = "3/16"
    uc_result = uc.news_crawler(datetime(2022,2,5))
    wc_result = wc.weather_crawler(datetime(2023,3,19))
    # start_date = datetime.strptime(start_date_str, "%m/%d")
    # pc_result = pc.get_articles_info(start_date=start_date)
    print("---------------- uc_result start crawler -------------------")
    print(uc_result)
    print("---------------- uc_result end crawler -------------------")
    print("---------------- wc_result start crawler -------------------")
    print(wc_result)
    print("---------------- wc_result end crawler -------------------")
    # print("---------------- pc_result start crawler -------------------")
    # print(pc_result)
    # print("---------------- pc_result end crawler -------------------")
    print("---------------- end crawler -------------------")
    return x
