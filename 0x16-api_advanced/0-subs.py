#!/usr/bin/python3
"""
working on the Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """working to Return the total num of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my-reddit-subscriber-script/0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
