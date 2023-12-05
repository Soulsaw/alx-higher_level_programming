#!/usr/bin/python3
""" implement error code with requests """
if __name__ == "__main__":
    """implementation of the error
    """
    import requests
    import sys
    """ Implementation """
    url = sys.argv[1]
    reponse = requests.get(url=url)
    if (reponse.status_code >= 400):
        print('Error code:', reponse.status_code)
    else:
        print(reponse.text)
