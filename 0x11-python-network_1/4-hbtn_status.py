#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status using 'request'"""
if __name__ == '__main__':
    import requests
    """importing the request module"""
    r = requests.get('https://alx-intranet.hbtn.io/status')
    r.raise_for_status()
    print('Body response:')
    print('\t- type:', type(r.text))
    print('\t- content:', r.text)
