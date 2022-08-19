#!/usr/bin/python3
"""Script the fetches: https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests

    url = 'https://intranet.hbtn.io/status'
    content = requests.get(url)
    print('Body response:')
    print("\t- type: {}".format(type(content.text)))
    print("\t- content: {}".format(content.text))
    content.close()
