#!/usr/bin/python3
"""
A function that queries the Reddit-API
"""

import requests


def number_of_subscribers(subreddit):
    """returns the total number of subscribers for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0
