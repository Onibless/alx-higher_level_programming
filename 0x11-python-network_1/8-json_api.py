#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status using 'request'"""
if __name__ == '__main__':
    import requests
    import sys
    """importing the request module"""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        result = r.json()
        if result == {}:
            print('No result')
        else:
            print("[{}] {}".format(result.get("id"), result.get("name")))
    except ValueError:
        print('Not a valid JSON')
