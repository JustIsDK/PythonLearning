import random
import redis

r = redis.Redis(host=xxx.xxx.xxx.xxx, port=xxx,password=xxx, db=0)
with r.pipeline(transaction=False) as p:
    i = 0
    while i < 100001:
        value = str(random.randint(0,100000))
        i+=1
        p.sadd(key, value)

    p.execute()
