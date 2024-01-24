# If needed:
# Pip install Tweepy if you don't already have the package
# !pip install tweepy

import tweepy
import pandas as pd
from datetime import datetime, timezone, timedelta

# Change this information with your own # licences.
client = tweepy.Client \
    (bearer_token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                       consumer_key="XXXXXXXXXXXXXXXXXXXXXXX", consumer_secret="XXXXXXXXXXXXXXXXXXXXXXXXX",
                       access_token="XXXXXXXXXXXXXXXXXXXXXXX",
                       access_token_secret="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

# Replace with the user ID you want to fetch tweets from
# Look up user's ID in this site: https://ilo.so/twitter-id/
query = 'UPDATE THIS INFO'

# Replace tweet_fields with the fields you want to retrieve
tweets = client.get_users_tweets(id=query, tweet_fields=['id', 'created_at', 'text', 'public_metrics'], max_results=100)

# Set the date range to fetch tweets from the year 2022
start_time_str = '2023-10-01 00:00:00+00:00'
end_time_str = '2023-12-31 23:59:59+00:00'

# Parse string times to datetime objects
start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S%z')
end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S%z')

# Create an empty list to store tweet data
tweets_list = []

# Iterate through the tweets and append data to the list
for tweet in tweets.data:
    # tweet['created_at'] is already a datetime object
    tweet_time = tweet['created_at']

    # Make start_time and tweet_time both aware datetime objects
    start_time = start_time.replace(tzinfo=timezone.utc)
    tweet_time = tweet_time.replace(tzinfo=timezone.utc)

    # Check if tweet is within the specified time period
    if start_time <= tweet_time <= end_time:
        public_metrics = tweet.get('public_metrics', {})
        tweets_list.append([tweet['id'], tweet['created_at'], tweet['text'], public_metrics.get('retweet_count', 0), public_metrics.get('favorite_count', 0)])

# Create a DataFrame from the list
tweets_df = pd.DataFrame(tweets_list, columns=['id', 'created_at', 'text', 'retweet_count', 'favorite_count'])

# Converting dataframe to CSV
tweets_df.to_csv(f'{query}-tweets.csv', sep=',', index=False)