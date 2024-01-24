# This code aims to scrap tweet from an specific user.

# If needed:
# Pip install Tweepy if you don't already have the package
# !pip install tweepy
# References: Martin Beck: https://towardsdatascience.com/how-to-scrape-tweets-from-twitter-59287e20f0f1
# Github: https://github.com/MartinBeckUT/TwitterScraper/blob/master/BasicScraper/Tweepy_Basic_Scraper.ipynb
# Another interesting reference to have in mind: https://sean-doody.github.io/socilabs/p/tweepy-twitter-tutorial/

import tweepy
import pandas as pd
import time

# Credentials and Authorization

consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Change this information with your own licences.
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Query by Username
# Creation of queries using Tweepy API
# Function is focused on completing the query then providing a CSV file of that query using pandas

tweets = []


def username_tweets_to_csv(username, count):
    try:
        # Creation of query method using parameters
        tweets = tweepy.Cursor(api.user_timeline, id=username).items(count)

        # Pulling information from tweets iterable object
        tweets_list = [[tweet.created_at, tweet.id, tweet.text, tweet.retweet_count, tweet.favorite_count]
                       for tweet in tweets]

        # Creation of dataframe from tweets list
        # Add or remove columns as you remove tweet information
        tweets_df = pd.DataFrame(tweets_list, columns={'Datetime', 'Tweet Id', 'Text', 'Retweet_count', 'favorite_count'})

        # Converting dataframe to CSV
        tweets_df.to_csv('{}-tweets.csv'.format(f"{username}_17_2_23"
                                                f""), sep=',', index=False)

    except BaseException as e:
        print('failed on_status,', str(e))
    time.sleep(3)


# Input username to scrape tweets and name csv file
# Max recent tweets pulls x amount of most recent tweets from that user
username = 'AfD' # Example
count = 20000


# Other user names used:
# 'AfD'
# 'Die_Gruenen'
# 'CDU'
# 'spdde'
# 'fdp'
# 'CSU'
# 'dieLinke'

# Calling function to turn username's past X amount of tweets into a CSV file
username_tweets_to_csv(username, count)
