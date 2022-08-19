#!/usr/bin/python3
"""Python script that takes in a URL, sends
a request to the URL and displays the body
of the response (decoded in utf-8)."""

if __name__ == "__main__":
    from sys import argv
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    from urllib.error import HTTPError

    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
