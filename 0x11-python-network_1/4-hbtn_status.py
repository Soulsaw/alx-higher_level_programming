#!/usr/bin/python3
"""requests get response
"""
if __name__ == "__main__":
    import requests
    """ Implementation """
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(req.text))
    print("\t- content:", req.text)
