#!/usr/bin/python3
""" Module for a function that queries the Reddit API."""


import requests


def recurse(subreddit, hot_list=[], after=''):
    """ A function that queries the Reddit API.
    Returns: A list containing the titles of all hot articles for
             a given subreddit or None if an invalid subreddit is given.
    """
    if after is None:
        return hot_list

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'redquery'}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(url, headers=header, params=parameters,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        hot = response.json()['data']['children']
        aft = response.json()['data']['after']
        for post in hot:
            hot_list.append(post['data']['title'])
    except Exception:
        return None

    return recurse(subreddit, hot_list, aft)
