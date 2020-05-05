import tweepy
from datetime import datetime

# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
consumer_key = "IRtAWN2xOvjmCue4lmQEkHNoQ"
consumer_secret = "veMK7T5audEbTegdB6gEm0uYnnco6dDp1JvEmciGd5vo5LF9Sx"
access_key = "-"
access_secret = ""

usernamelist = ["GovLarryHogan", "GavinNewsom", "CDCgov", "WHO", "WhiteHouse", "NIAIDNews"]
numberOfTweets = 10

try:
    # Authorization to consumer key and consumer secret
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    # Calling api
    api = tweepy.API(auth)
except:
    print("Error: Missing API keys")



# hold tweets as python dicts
data = []

# Function to extract tweets
def get_tweets02(username):


    # Iterate thru tweets
    for tweet in tweepy.Cursor(api.user_timeline, screen_name = username, tweet_mode = 'extended').items(1):
        #print(tweet.id)
        #print(tweet.user.name +": "+ str(tweet.user.id))
        #print(tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S"))
        tweet_info = {
                    'tweet_id': tweet.id,
                    'name': tweet.user.screen_name,
                    #'screen_name': tweet.user.screen_name,
                    #'retweet_count': tweet.retweet_count,
                    'text': tweet.full_text,
                    #'time_read_at': datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                    'created': tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
                    #'favourite_count': tweet.favorite_count,
                    'source_url': tweet.source_url
                }
        data.append(tweet_info)
    return data

def testsources():
    for i in usernamelist: 
        get_tweets02(i) 

#testsources()

def getTweets():
    '''
    user id list: Governor Larry Hogan, Gavin Newsom, CDC, World Health Organization (WHO), 
    The White House, NIAID News
    '''
    
    useridlist = [2987671552, 11347122, 146569971, 
                    14499829, 822215673812119553, 59769395]

    # 
    for userid in useridlist: 
            # Iterate thru tweets
        for tweet in tweepy.Cursor(api.user_timeline, user_id = userid, tweet_mode = 'extended').items(numberOfTweets):
            
            print(tweet.user.name +": "+ str(tweet.id))
            #print(tweet)
            
            tweet_info = {
                    'tweet_id': tweet.id,
                    'name': tweet.user.screen_name,
                    #'screen_name': tweet.user.screen_name,
                    #'retweet_count': tweet.retweet_count,
                    'text': tweet.full_text,
                    #'time_read_at': datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                    'created': tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
                    #'favourite_count': tweet.favorite_count,
                    'source_url': tweet.source_url
                }
            data.append(tweet_info)
    return data
        

#getTweets()