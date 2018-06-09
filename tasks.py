from celery import Celery
import time

app = Celery('tasks', broker='pyamqp://rooty:passy@rabbitmq//', backend='rpc://')

@app.task
def add(x, y):
    time.sleep(0.1)
    return x + y

if __name__=='__main__':
    add.delay(4, 4)
