#!/usr/bin/python3
"""
This script returns information about the TODO list of a given employee
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = "https://https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todo = requests.get(url + "todo", params={"userId": argv[1]}).json()
    done = [t.get("title") for t in todo if t.get("done") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todo)))
    [print("\t {}".format(c)) for c in completed]
