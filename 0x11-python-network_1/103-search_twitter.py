#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
from requests import get
from sys import argv


if __name__ == "__main__":
    res = get(argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
