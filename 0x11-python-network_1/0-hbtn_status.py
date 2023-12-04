#!/usr/bin/python3
"""urllib exploration
"""
if __name__ == "__main__":
    import urllib.request
    """ Implementation """
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        content = response.read()
        decoded_content = content.decode('utf-8')

        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", decoded_content)
