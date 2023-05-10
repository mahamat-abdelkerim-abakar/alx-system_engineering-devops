#!/usr/bin/python3
<<<<<<< HEAD
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import re
import requests
import sys


def add_title(dictionary, hot_posts):
    """ Adds item into a list """
    if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].split()
    for word in title:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(word):
                dictionary[key] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    """ Queries to Reddit API """
    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts)
    after = dic['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list):
    """ Init function """
    dictionary = {}

    for word in word_list:
        dictionary[word] = 0

    recurse(subreddit, dictionary)

    l = sorted(dictionary.items(), key=lambda kv: kv[1])
    l.reverse()

    if len(l) != 0:
        for item in l:
            if item[1] is not 0:
                print("{}: {}".format(item[0], item[1]))
    else:
        print("")
=======
"""Contains the count_words function"""
import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    '''Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        found_list (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
    '''
    user_agent = {'User-agent': 'test45'}
    posts = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                         .format(subreddit, after), headers=user_agent)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if posts.status_code == 200:
        posts = posts.json()['data']
        aft = posts['after']
        posts = posts['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)
        if aft is not None:
            count_words(subreddit, word_list, found_list, aft)
        else:
            result = {}
            for word in found_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return
>>>>>>> 5798a831616d10085e34bce5e536e49f08e3b4cb
