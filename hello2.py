from flask import Flask, redirect, url_for, request, render_template
import tweepy
import codecs
from textblob import TextBlob 
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

#Twitter authorization stuff
consumer_key = 'xCVooH1T1Ao9rjEBvMnC9QR3u'
consumer_secret = 'wFau0GNQFgB1n4iDoGdQ9geqsXiwLpYoV0iak8Mh0AwT73mZLY'
access_token = '214512527-MEdGSOfpBlKplFzudxZwlQQm5Fl6jr84hZIEVRwS'
access_secret = 'ypLZOrgCbIUbHsUNfQN7Z1z9DovSgmZwqlpVjNhzGX06o'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret) 
api = tweepy.API(auth)
#Flask code
app = Flask(__name__)

#some variables

#here
hasht = 'abc'
@app.route('/index', methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':
		global hasht
		hasht = request.form['hasht']
		return redirect(url_for('hashtagCompute', name=hasht))

#Get hashtag here  
@app.route('/hashtag=<name>')
def hashtagCompute(name):
	neg=0
	pos=0
	x=0
	count=0
	for tweet in tweepy.Cursor(api.search,q=name,count=100,lang="en",since_id=2016-10-11).items():
		count=count+1
		if(count==501):
			break
		#print tweet.created_at, tweet.text
		#f.write("%s,%s\ufeff" %(tweet.created_at, tweet.text))

		blob=TextBlob(tweet.text)
		for sentence in blob.sentences:
			x+=sentence.sentiment.polarity
		if(x<0):
			neg=neg+1
		else:
			pos=pos+1

	return render_template('untitledtemplate.html', htmlhashtag=hasht, postweets=pos, negtweets=neg)
	




if __name__ == '__main__':
   app.run(debug = True)