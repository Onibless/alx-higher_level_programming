#!/usr/bin/python3
"""script that takes in a URL, sends
a request to the URL and displays the
body of the response (decoded in utf-8)."""
if __name__ == '__main__':
    import urllib.request as u_req
    import urllib.error as u_err
    import sys
    """Importing urllib module and sys for user input via terminal"""
    # req = u_req.Request(sys.argv[1])
    try:
        with u_req.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except u_err.HTTPError as e:
        print("Error code:", e.code)
