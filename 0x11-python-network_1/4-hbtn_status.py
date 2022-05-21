#!/usr/bin/python3
"""Fetches the status of a URL with requests lib."""
import requests

if __name__ == '__main__':
    status = requests.get('https://intranet.hbtn.io/status')
    print('Body response:\n\t- type: {}\n\t- content: {}'
          .format(type(status.text), status.text))
    """
    Body response:
        - type: <class 'str'>
        - content: OK
    """
