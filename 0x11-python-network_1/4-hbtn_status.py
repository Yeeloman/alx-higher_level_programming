#!/usr/bin/python3
"""a Python script that fetches
https://alx-intranet.hbtn.io/status"""


import requests as reqs
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    resp = reqs.get(url)
    print("Body response:")
    print("    - type:", type(resp.text))
    print("    - content:", resp.text)
