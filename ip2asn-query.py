import ipaddress
import redis
import json
import datetime


def isBogon(ip):
    ip_address = ipaddress.ip_address(ip)

    networks = [
        "0.0.0.0/8",
        "10.0.0.0/8",
        "100.64.0.0/10",
        "127.0.0.0/8",
        "169.254.0.0/16",
        "172.16.0.0/12",
        "192.0.0.0/24",
        "192.0.2.0/24",
        "192.88.99.0/24",
        "192.168.0.0/16",
        "198.18.0.0/15",
        "198.51.100.0/24",
        "203.0.113.0/24",
        "240.0.0.0/4",
        "255.255.255.255/32",
        "224.0.0.0/4",
    ]

    for network in networks:
        if ip_address in ipaddress.ip_network(network):
            return True

    return False


redisClient = redis.Redis(host='localhost', port=6379, db=0)

ip = input('Digite o endereço IP: ')

if isBogon(ip):
    print('Bogon IP Address!')
    exit(1)

startTime = datetime.datetime.now()

value = redisClient.zrangebyscore('ip_table', int(
    ipaddress.ip_address(ip)), '+inf', 0, 1)

endTime = datetime.datetime.now()
deltaTime = endTime-startTime

print(json.loads(value[0].decode('utf8')))
print('Tempo para responder: {}ms'.format(deltaTime.total_seconds() * 1000))

redisClient.close()
