#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
from requests import get, auth
from sys import argv


if __name__ == "__main__":
    res = get("https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])).json()
    c = 0
    for lines in res:
        print("{}: {}".format(lines.get('sha'),
                             lines.get('commit').get('author').get('name')))
        c += 1
        if c == 10:
            break
