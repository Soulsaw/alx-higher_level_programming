#!/usr/bin/python3
"""urllib exploration
"""
if __name__ == "__main__":
    import urllib.request
    import sys
    """ Implementation """
    url = sys.argv[1]
    data = 'email={}'.format(sys.argv[2])
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
