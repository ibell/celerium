from tasks import add
from celery import group

r = group(add.s(i, i) for i in range(1000000)).apply_async()
print(r.get())
