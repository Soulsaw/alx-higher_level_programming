#!/usr/bin/python3
"""requests post exploration
"""
if __name__ == "__main__":
    import requests
    import sys
    """ Implementation """
    token = sys.argv[2]
    username = sys.argv[1]
    url = 'https://api.github.com/users/{}'.format(username)
    header = {'Accept': 'application/vnd.github+json',
              'Authorization': f'Bearer {token}'
              }
    req = requests.get(url, headers=header)
    json = req.json()
    if 'id' in json:
        print(json['id'])
    else:
        print('None')
