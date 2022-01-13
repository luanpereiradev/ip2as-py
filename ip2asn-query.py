import ipaddress
import redis
import json
import datetime

r = redis.Redis(host='localhost', port=6379, db=0)

ip = input('Digite o endereço IP: ')

a = datetime.datetime.now()

value = r.zrangebyscore('ip_table', int(
    ipaddress.ip_address(ip)), 'inf', 0, 1)

b = datetime.datetime.now()
delta = b-a

print(json.loads(value[0].decode('utf8')))
print('Tempo para responder: {}ms'.format(delta.total_seconds() * 1000))

r.close()
