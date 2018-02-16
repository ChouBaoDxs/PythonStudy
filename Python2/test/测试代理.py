# -*- coding: UTF-8 -*-

import requests

url = 'https://httpbin.org/ip'

proxy = {
    'http': 'http://121.232.146.101:9000',
    'https': 'http://121.232.146.101:9000'
}

print(requests.get(url, proxies=proxy).text)
