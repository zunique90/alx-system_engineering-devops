#!/usr/bin/python3
"""recursive function that queries the Reddit API"""

import requests


def count_words(subreddit, word_list, hot_list=[], after=""):
    """prints a sorted count of given keywords"""
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
        count_words(subreddit, word_list, hot_list, after)
    return hot_list
