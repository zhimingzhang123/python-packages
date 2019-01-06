# coding:utf-8
from celery import task,shared_task

@shared_task
def add(a,b):
    print('任务执行。。。。')
    print(a+b)
    return a + b

@shared_task
def running():
    print('10秒钟执行一次....')
