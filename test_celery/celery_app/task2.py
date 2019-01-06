import time
from celery_app import app


@app.task
def add_plus(x, y):
    time.sleep(6)
    return (x + y) * 2
