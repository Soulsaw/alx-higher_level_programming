#!/usr/bin/python3
"""requests post exploration
"""
if __name__ == "__main__":
    import requests
    import sys
    """ Implementation """
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    req = requests.post(url=url, data=data)
    print(req.text)
