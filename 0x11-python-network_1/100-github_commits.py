#!/usr/bin/python3
"""requests post exploration
"""
if __name__ == "__main__":
    import requests
    import sys
    """ Implementation """
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner_name,
                                                              repository_name)
    req = requests.get(url=url)
    results = req.json()
    for i in range(0, 10, 1):
        print(results[i]['sha'], results[i]['commit']['author']['name'],
              sep=': ')
