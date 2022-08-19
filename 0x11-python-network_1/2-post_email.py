#!/usr/bin/python3
"""Python script that takes in a URL, sends
a request to the URL and displays the body
of the response (decoded in utf-8)."""

if __name__ == "__main__":
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
        print(the_page.decode('utf-8'))
