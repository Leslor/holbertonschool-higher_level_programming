#!/usr/bin/python3
"""Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as
a parameter, and finally displays the body of the response. """

if __name__ == "__main__":
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth

    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(argv[1], argv[2])
    content = requests.get(url, auth=auth)
    print(content.json().get("id"))
