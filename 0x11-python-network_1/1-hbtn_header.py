#!/usr/bin/python3
"""script that takes in a URL, sends a request to
the URL and displays the value of the X-Request-Id
variable found in the header of the response."""
if __name__ == '__main__':
    import urllib.request as u_req
    import sys
    """Importing urllib module and sys for user input via terminal"""
    if len(sys.argv) > 1:
        with u_req.urlopen(sys.argv[1]) as response:
            print(response.info()['X-Request-Id'])
