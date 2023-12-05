#!/usr/bin/python3
""" Implementation of json api """
if __name__ == "__main__":
    """ Import module """
    import sys
    import requests
    """ Implementation """
    data = {'q': sys.argv[1] if len(sys.argv) > 1 else ''}
    url = 'http://0.0.0.0:5000/search_user'
    res = requests.post(url=url, data=data)
    json = res.json()
    if len(json) == 0:
        print('No result')
    else:
        print('[{}] {}'.format(json['id'], json['name']))
