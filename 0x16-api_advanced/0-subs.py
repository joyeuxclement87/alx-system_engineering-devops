#!/usr/bin/python3
"""
workin on the Module to the number of subscribers for a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the total number of subscribers on a given subreddit.

    Args:
        subreddit (str): The subreddit name.

    Returns:
        int: The number of subscribers if the subreddit exists, 0 otherwise.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
    except requests.RequestException:
        pass
    return 0
