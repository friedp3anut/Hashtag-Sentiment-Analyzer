import tweepy
import codecs
from textblob import TextBlob 
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'xCVooH1T1Ao9rjEBvMnC9QR3u'
consumer_secret = 'wFau0GNQFgB1n4iDoGdQ9geqsXiwLpYoV0iak8Mh0AwT73mZLY'
access_token = '214512527-MEdGSOfpBlKplFzudxZwlQQm5Fl6jr84hZIEVRwS'
access_secret = 'ypLZOrgCbIUbHsUNfQN7Z1z9DovSgmZwqlpVjNhzGX06o'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
hashtag = raw_input("Enter hashtag here: ")
f = codecs.open('file.txt','w',encoding='utf-8')
neg=0
pos=0
x=0
count=0
for tweet in tweepy.Cursor(api.search,q=hashtag,count=100,lang="en",since_id=2016-10-11).items():
	count=count+1
	if(count==501):
		break
	print tweet.created_at, tweet.text
	f.write("%s,%s\ufeff" %(tweet.created_at, tweet.text))

	blob=TextBlob(tweet.text)
	for sentence in blob.sentences:
		x+=sentence.sentiment.polarity
	if(x<0):
		neg=neg+1
	else:
		pos=pos+1


f.close()
print "number of pos tweets:"
print pos
print "number of neg tweets:"
print neg

if(neg>pos):
	print "TOTAL NEG"
else:
	print "TOTAL POS"