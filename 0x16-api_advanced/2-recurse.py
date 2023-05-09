#!/usr/bin/python3
"""recursive function that queries the Reddit API"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    returns a list of titles of all hot articles for a given subreddit
    """
    url = ("https://www.reddit.com/r/{}/hot.json".format(subreddit))
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"t": all, "after": after}
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
            )
    if not response or response.status_code != 200:
        return None
    data = response.json()
    for hot in data["data"]["children"]:
        hot_list.append(hot["data"]["title"])
    after = data.get("data").get("after")
    if after:
        recurse(subreddit, hot_list, after)
    return hot_list
