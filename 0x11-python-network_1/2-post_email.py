#!/usr/bin/python3
from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode

url = argv[1]
value = {'email': argv[2]}
data = urlencode(value)
data = data.encode('ascii')
req = Request(url, data)
with urlopen(req) as response:
    the_page = response.read()
    print("THE PAGE")
    print(the_page.decode('utf-8'))
