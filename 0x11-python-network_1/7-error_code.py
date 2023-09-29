#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status using 'request'"""
if __name__ == '__main__':
    import requests
    import sys
    """importing the request module"""
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print('Error code:', r.status_code)
    else:
        print(r.text)
