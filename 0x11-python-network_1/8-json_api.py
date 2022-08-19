#!/usr/bin/python3
"""Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as
a parameter, and finally displays the body of the response. """

if __name__ == "__main__":
    import requests
    from sys import argv
    url = "http://0.0.0.0:5000/search_user"
    json = {}
    if (len(argv) == 2 and isinstance(argv[1], str)):
        json = {'q': argv[1]}
    else:
        json = {'q': ''}
    try:
        content = requests.post(url, data=json)
        response = conten.json()
        if (response == {}):
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
