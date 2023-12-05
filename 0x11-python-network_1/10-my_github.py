#!/usr/bin/python3
"""requests post exploration
"""
if __name__ == "__main__":
    import requests
    import sys
    """ Implementation """
    url = 'https://api.github.com/users'
    username = sys.argv[1]
    token = sys.argv[2]
    data = {"username": username, "password": token}
    req = requests.get(url=url, data=data)
    json = req.json()
    if 'id' in json:
        print(json['id'])
    else:
        print("None")
