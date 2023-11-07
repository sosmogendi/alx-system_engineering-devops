#!/usr/bin/python3
"""
This module provides a recursive function to query the Reddit API, parse hot articles' titles, and print a sorted count of given keywords.
"""

import requests

def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursively query the Reddit API, parse hot articles' titles, and print a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        after (str): The Reddit API parameter for pagination (optional).
        count_dict (dict): A dictionary to store keyword counts (optional).

    Returns:
        None
    """
    # Initialize count_dict if it's None
    if count_dict is None:
        count_dict = {}

    # Define the Reddit API endpoint for the given subreddit, including the 'after' parameter for pagination
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'myRedditBot/1.0'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response to extract the titles and the 'after' parameter
        data = response.json()
        posts = data['data']['children']
        after = data['data']['after']

        # If there are posts, accumulate keyword counts
        if posts:
            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    # Check if the word is in the title (case-insensitive)
                    if f" {word.lower()} " in f" {title} ":
                        # Increment the count in count_dict
                        count_dict[word.lower()] = count_dict.get(word.lower(), 0) + 1

            # If there's an 'after' parameter, recursively call the function for the next page
            if after is not None:
                return count_words(subreddit, word_list, after, count_dict)
            else:
                # Sort the counts in descending order by count and then alphabetically by keyword
                sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))

                # Print the sorted counts
                for word, count in sorted_counts:
                    print(f"{word}: {count}")

                return None
        else:
            return None
    else:
        return None

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        keywords = [x for x in sys.argv[2].split()]
        count_words(subreddit, keywords)
