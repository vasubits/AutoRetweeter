import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import tweepy
import time,json
import numpy as np
import tweepy as TweepError


APP_KEY="write own"
APP_SECRET="write own"
OAUTH_TOKEN="write own"
OAUTH_TOKEN_SECRET="write own"
username=raw_input(" find retweet all tweets of : ")
auth = tweepy.OAuthHandler(APP_KEY,APP_SECRET)
auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

count=0

api = tweepy.API(auth)
u=api.get_user(screen_name='vasu_test')
my=u.id
print my

flag=0
row_num = 500
col_num = 2
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for status in api.user_timeline(screen_name=username,include_rts=0,count=200):
	count+=1
#print ("no. of total tweets of given user%d"%count)
for j in range(0,count,1):
    firstTweet = api.user_timeline(screen_name=username,include_rts=0,count=200)[j]
    if hasattr (firstTweet, 'retweeted_status'):
    	# get the original tweet
    	original_tweet = firstTweet.retweeted_status.id
    	# iterate over retweets to get user id
	
    	for status1 in api.retweets(original_tweet):
	  # b=np.where(a==status1.user.id)
	   b=status1.user.id
         #  print(b)
	   if(b==my):
	     flag=1
	    # print("flag = %d")%flag
	     break
	   else:
             flag=0
            # print("flag = %d")%flag
    
   	if(flag==0):
		 api.retweet(firstTweet.id)
		 print("retweeted")
   
print("done...")
         
