#!/usr/bin/python3
"""Python script that takes in a URL,
sends a request to the URL and displays
the value of the variable X-Request-Id in the response headers"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    content = requests.get(url)
    print(content.headers.get('X-Request-Id'))
    content.close()
