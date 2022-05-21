#!/usr/bin/python3
"""Sends a POST request."""
import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    response = requests.post(url, data={"q": letter})
    try:
        r = response.json()
        if r:
            print("[{}] {}".format(r.get("id"), r.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
