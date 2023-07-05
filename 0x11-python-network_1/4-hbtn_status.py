#!/usr/bin/python3
"""fetches https://0.0.0.0:5050/status."""
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
