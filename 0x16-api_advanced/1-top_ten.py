#!/usr/bin/python3
"""A function that queries the Reddit API"""

import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    """
    url = ("https://www.reddit.com/r/{}/hot.json".format(subreddit))
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for hot in data["data"]["children"][:10]:
            print(hot["data"]["title"])
    else:
        print("None")
