#!/usr/bin/python3
<<<<<<< HEAD
"""function that queries the Reddit API and returns the number of subscribers
for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the number of
    subscribers for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
=======
""" Function that queries the Reddit API """
import requests
import sys


def number_of_subscribers(subreddit):
    """  Args:
        subreddit: subreddit name
    Returns:
        number of subscribers to the subreddit,
        or 0 if subreddit requested is invalid"""
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
>>>>>>> 5798a831616d10085e34bce5e536e49f08e3b4cb
