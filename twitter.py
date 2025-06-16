import os
from dotenv import load_dotenv
import tweepy
import requests

load_dotenv()


twitter_client = tweepy.Client(
    bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
    consumer_key=os.environ["TWITTER_API_KEY"],
    consumer_secret=os.environ["TWITTER_API_KEY_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
)


def scrape_user_tweets(username, num_tweets=5):
    """
    Scrapes a Twitter user's original tweets (i.e., not retweets or replies) and returns them as a list of dictionaries.
    Each dictionary has three fields: "time_posted" (relative to now), "text", and "url".
    """
    user_id = twitter_client.get_user(username=username).data.id
    tweets = twitter_client.get_users_tweets(
        id=user_id, max_results=num_tweets, exclude=["retweets", "replies"]
    )

    tweet_list = []
    for tweet in tweets.data:
        tweet_dict = {}
        tweet_dict["text"] = tweet["text"]
        tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet.id}"
        tweet_list.append(tweet_dict)

    return tweet_list


def scrape_user_tweets_mock(username="EdenEmarco177", num_tweets=5):
    """
    Generates mock tweets for testing purposes.
    Each dictionary has fields: "text" and "url".
    """
    # Generate some generic tweets
    mock_tweets = [
        {
            "text": "Just finished an amazing book! Always learning and growing.",
            "id": "1234567890"
        },
        {
            "text": "Beautiful day for outdoor activities. Nature is rejuvenating!",
            "id": "1234567891"
        },
        {
            "text": "Excited about new opportunities and challenges ahead.",
            "id": "1234567892"
        },
        {
            "text": "Great meeting with the team today. Collaboration leads to success!",
            "id": "1234567893"
        },
        {
            "text": "Reflecting on personal growth and future goals.",
            "id": "1234567894"
        }
    ]

    tweet_list = []
    for tweet in mock_tweets:
        tweet_dict = {}
        tweet_dict["text"] = tweet["text"]
        tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet['id']}"
        tweet_list.append(tweet_dict)

    return tweet_list


if __name__ == "__main__":

    tweets = scrape_user_tweets_mock(username="EdenEmarco177")
    print(tweets)
