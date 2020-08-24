#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    data = parse.urlencode({'email': argv[2]}).encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
