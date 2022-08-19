#!/usr/bin/python3
"""Script the fetches: https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    import urllib.request

    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')
        print('Body response:')
        print(f'\t- type: {type(content)}')
        print(f'\t- content: {content}')
        print(f'\t- utf8 content: {utf8_content}')
