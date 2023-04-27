import importlib
import typing

from worker import app
import sys
sys.path.append("./crawler")

# 註冊 task, 有註冊的 task 才可以變成任務發送給 rabbitmq
@app.task()
def crawler(dataset: str,parameters: typing.Dict[str, str],):
    # 使用 getattr, importlib,
    # 根據不同 dataset, 使用相對應的 crawler 收集資料
    # 爬蟲
    # df = getattr(importlib.import_module(f"crawler.{dataset}"),"crawler",)(parameters=parameters)
    # df = getattr(importlib.import_module(f"crawler.{dataset}"))(parameters=parameters)
    # print(df)
    getattr(print(f"{dataset} {parameters}"))(parameters=parameters)
    print("crawler")
    print("upload db")
