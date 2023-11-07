#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and print the titles of the first 10 hot posts for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Query the Reddit API and print the titles of the first 10 hot posts for the given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    # Define the Reddit API endpoint for the given subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'myRedditBot/1.0'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response to extract the titles of the first 10 hot posts
        data = response.json()
        posts = data['data']['children']

        if not posts:
            print("No hot posts found in this subreddit.")
        else:
            for i, post in enumerate(posts, 1):
                print(f"{i}. {post['data']['title']}")
    else:
        print("None")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
