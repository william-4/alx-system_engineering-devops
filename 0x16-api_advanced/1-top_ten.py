#!/usr/bin/python3
""" Module for a function that queries the Reddit API."""


import requests


def top_ten(subreddit):
    """ A function that queries the Reddit API.
    Prints the titles of the first 10 hot posts listed for a given subreddit
    or None if an invalid subreddit is given
    """

    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    header = {'user-agent': 'redquery'}
    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return None

    try:
        hot = response.json()['data']['children']
        for post in hot[:10]:
            print(post['data']['title'])
    except Exception:
        print(None)
