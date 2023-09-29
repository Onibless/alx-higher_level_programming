#!/usr/bin/python3
"""script which fetches https://alx-intranet.hbtn.io/status"""
if __name__ == '__main__':
import urllib.request
 """Importing urllib module"""
    req = u_request.Request('https://alx-intranet.hbtn.io/status')
    with u_request.urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode('utf-8'))
