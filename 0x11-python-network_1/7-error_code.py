#!/usr/bin/python3
"""Python script that takes in a URL, sends
a request to the URL and displays the body
of the response."""

if __name__ == "__main__":
    import requests
    from sys import argv
    url = requests.get(argv[1])
    status = url.status_code
    if (status >= 400):
        print('Error code: {}'.format(status))
    else:
        print(url.text)
