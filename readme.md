##### 1.python-celery4.x

##### 2.Django结合celery4.x

```js
CELERYD_FORCE_EXECV = True  // 可以防止死锁， 4.0中取消此设置，django-celery可以使用
CELERYD_CONCURRENCY = 8 // 设置worker的并发数量，一般和cpu数量一样
CELERY_ACKS_LATE = True // 允许重试。在4.0中更改了名称 (http://docs.celeryproject.org/en/latest/history/whatsnew-4.0.html?highlight=CELERY_ACKS_LATE)
CELERYD_MAX_TASKS_PER_CHILD = 100 // 每个worker执行多少个任务后销毁
CELERYD_TASK_TIME_LIMIT // 单个任务的允许运行的最大时间 ，4.0中已更名
CELERY_QUEUES // 指定队列，4.0更推荐使用task_queues http://docs.celeryproject.org/en/latest/userguide/routing.html#routing-automatic
```

##### 3. flower和supervisor监控和部署celery (未完成)

```
完成了celery在supervisor的配置， 在celery-example中
```

