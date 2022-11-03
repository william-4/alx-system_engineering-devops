#!/usr/bin/python3
""" Module for a function that queries the Reddit API."""


import requests


def number_of_subscribers(subreddit):
    """ A function that queries the Reddit API.
    Returns: Number of subscribers for a given subreddit or
             0 if an invalid subreddit is given
    """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'user-agent': 'redquery'}
    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        return response.json()['data']['subscribers']
    except Exception:
        return 0
