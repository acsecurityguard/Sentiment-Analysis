from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s



#consumer key, consumer secret, access token, access secret.
ckey="8nrLOAHyA2rSE58mvSTU8nRKs"
csecret="bKGIAIdu4EVIR8y3xWEe5tPMXYJLh90gBP1lXpwmlF2ucwqIHU"
atoken="45048751-BcZNLvRgbiILNesbSLyBrenBtMJCIKslueQYxxuwO"
asecret="pJRsORRCsEMkwX2TsOfHvdXpN13P5ew1CYXlBa37dTupM"

#from twitterapistuff import *

class listener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)

            tweet = all_data["text"]
            sentiment_value, confidence = s.sentiment(tweet)
            print(tweet, sentiment_value, confidence)

            if confidence*100 >= 80:
                output = open("twitter-out.txt","a")
                output.write(sentiment_value)
                output.write('\n')
                output.close()

            return True
        except:
            return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["eur",])


