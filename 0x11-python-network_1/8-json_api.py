#!/usr/bin/python3
""" Implementation of json api """
if __name__ == "__main__":
    """ Import module """
    import sys
    import requests
    """ Implementation """
    data = {'q': sys.argv[1] if len(sys.argv) > 1 else ''}
    url = 'http://0.0.0.0:5000/search_user'
    try:
        res = requests.post(url=url, data=data)
        json = res.json()
        if not json:
            print('No result')
        else:
            print('[{}] {}'.format(json['id'], json['name']))
    except ValueError:
        print('Not a valid JSON')
