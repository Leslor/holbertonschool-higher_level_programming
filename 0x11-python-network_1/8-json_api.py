#!/usr/bin/python3
"""Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as
a parameter, and finally displays the body of the response. """

if __name__ == "__main__":
    import requests
    from sys import argv
    url = "http://0.0.0.0:5000/search_user"
    jsond = {}
    if (len(argv) == 2):
        jsond = {'q': argv[1]}
    else:
        jsond = {'q': ''}
    content = requests.post(url, data=jsond)
    try:
        response = content.json()
        if (response == {}):
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except:
        print("Not a valid JSON")
