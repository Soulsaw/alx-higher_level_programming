#!/usr/bin/python3
"""requests post exploration
"""
if __name__ == "__main__":
    import requests
    import sys
    """ Implementation """
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    headers = {'Accept': 'application/vnd.github+json'}
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner_name,
                                                              repository_name)
    req = requests.get(url=url, headers=headers)
    results = req.json()
    if req.status_code == 200:
        for commit in results[:10]:
            sha = commit['sha']
            auth_name = commit['commit']['author']['name']
            print(sha, auth_name, sep=': ')
