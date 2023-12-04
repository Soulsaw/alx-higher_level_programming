#!/usr/bin/python3
""" implement nothing """
if __name__ == "__main__":
    """implementation of the error
    """
    import urllib.request
    import sys
    """ Implementation """
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as reponse:
            content = reponse.read()
            decode = content.decode('utf-8')
            print(decode)
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
