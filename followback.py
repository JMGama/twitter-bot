import tweepy
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

# Initialize, authorize and connect with the Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Get the authenticated user's information.
me = api.me()

# Follow all the accounts that follow the bot.
for follower in tweepy.Cursor(api.followers).items():

    # Get the frienship info with the follower.
    _, follower_friendship = api.show_friendship(
        target_screen_name=follower.screen_name)

    # If the authenticated user is not following the user, then they start following it.
    if not follower_friendship.following:
        follower.follow()
