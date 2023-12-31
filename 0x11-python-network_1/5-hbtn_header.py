#!/usr/bin/python3
"""requests get retreiving X-Request-Id content
"""
if __name__ == "__main__":
    import requests
    import sys
    """ Implementation """
    req = sys.argv[1]
    response = requests.get(req)
    if response.status_code == 200:
        print(response.headers['X-Request-Id'])
