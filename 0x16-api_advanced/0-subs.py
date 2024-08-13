#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and retrieve the number of subscribers for a given subreddit.

Functions:
    number_of_subscribers(subreddit): Returns the number of subscribers for the specified subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to return the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit. Returns 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my-reddit-subscriber-script/0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
