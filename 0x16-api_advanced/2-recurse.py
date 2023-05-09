#!/usr/bin/python3
"""recursive function that queries the Reddit API"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list of titles of all hot articles for a given subreddit
    """
    url = ("https://www.reddit.com/r/{}/hot.json".format(subreddit))
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
            )
    if response.status_code == 200:
        data = response.json()
        if not data["data"]["children"]:
            return hot_list
        for hot in data["data"]["children"]:
            hot_list.append(hot["data"]["title"])
        after = data["data"]["after"]
        recurse(subreddit, hot_list, after)
    else:
        return None
    return hot_list
