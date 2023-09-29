#!/usr/bin/python3
"""script that takes in a URL and an email, sends a
POST request to the passed URL with the email as a
parameter, and displays the body of the response
(decoded in utf-8)"""
if __name__ == '__main__':
    import urllib.request as u_req
    import urllib.parse as u_per
    import sys
    """Importing urllib module and sys for user input via terminal"""
    data = u_per.urlencode({'email': sys.argv[2]}).encode('utf-8')
    with u_req.urlopen(sys.argv[1], data) as response:
        print(response.read().decode('utf-8'))
