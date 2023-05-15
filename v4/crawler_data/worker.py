# import importlib
# import socket
import time
import typing
import pymysql
from loguru import logger
from celery import Celery, Task
import db
from db.env_setting_pk.config import (
    MESSAGE_QUEUE_HOST,
    MESSAGE_QUEUE_PORT,
    WORKER_ACCOUNT,
    WORKER_PASSWORD,
)

broker = (
    f"pyamqp://{WORKER_ACCOUNT}:{WORKER_PASSWORD}@{MESSAGE_QUEUE_HOST}:{MESSAGE_QUEUE_PORT}/"
)

app = Celery(
    "task",
    # 只包含 tasks.py 裡面的程式, 才會成功執行
    include=["tasks"],
    # 連線到 rabbitmq,
    # pyamqp://user:password@localhost:5672/
    broker = broker,
)
