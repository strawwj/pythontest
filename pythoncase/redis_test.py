import redis
r = redis.Redis()
r.set('key1','hello world')
r.get('key1')
print(r.get('key1')).decode())

