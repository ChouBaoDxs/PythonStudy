# -*- coding: UTF-8 -*-
import ssl
from urllib.request import urlopen
ssl._create_default_https_context=ssl._create_unverified_context

html=urlopen("https://en.wikipedia.org/robots.txt")

print(html.read().decode('utf-8'))






