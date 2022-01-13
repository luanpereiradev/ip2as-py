import csv
import ipaddress
import json
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

with open("ip2asn-v4.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for row in rd:
        mapped = {
            'start_ip': row[0],
            'end_ip': row[1],
            'as': {
                'asn': int(row[2]),
                'name': row[4],
                'country': row[3],
            },
        }
        score = int(ipaddress.ip_address(row[1]))
        r.zadd('tabela_ip', {json.dumps(mapped): score})
        print(mapped)

r.close()
