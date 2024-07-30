#!/usr/bin/python3
"""THE use Reddit API and returnsthe number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """TO Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "THE User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
