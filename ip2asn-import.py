import csv
import ipaddress
import json
import redis

redisClient = redis.Redis(host='localhost', port=6379, db=0)
redisClient.delete('ip_table')

with open("dbip-asn-lite-2022-01.csv") as fd:
    rd = csv.reader(fd)
    for row in rd:
        as_name = row[3].lstrip("\"").rstrip("\"")
        as_number = int(row[2])

        if ipaddress.ip_address(row[0]).version == 4:
            mapped = {
                'start_ip': row[0],
                'end_ip': row[1],
                'as': {
                    'asn': as_number,
                    'name': as_name,
                },
            }
            score = int(ipaddress.ip_address(row[1]))
            redisClient.zadd('ip_table', {json.dumps(mapped): score})
            print(row)

redisClient.close()
