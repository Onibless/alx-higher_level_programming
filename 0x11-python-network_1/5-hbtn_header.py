#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status using 'request'"""
if __name__ == '__main__':
    import requests
    import sys
    """importing the request module"""
    r = requests.get(sys.argv[1])
    r.raise_for_status()
    print(r.headers.get('X-Request-Id'))
