#!/usr/bin/python3
if __name__ == "__main__":
    """
    """
    import urllib.request
    import urllib.error
    import sys
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as reponse:
            content = reponse.read()
            decode = content.decode('utf-8')
            print(decode)
    except urllib.error.URLError as e:
        print('Error code:', e.code)
