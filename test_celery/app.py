from celery_app import task1, task2


if __name__ == '__main__':
    task1.add.delay(1,2)
    task2.add_plus.delay(5,5)
    print('end ...')