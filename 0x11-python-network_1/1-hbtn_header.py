#!/usr/bin/python3
"""urllib exploration
"""
if __name__ == "__main__":
    import urllib.request
    import sys
    """ Implementation """
    req = sys.argv[1]
    with urllib.request.urlopen(req) as response:
        print(response.headers['X-Request-Id'])
