import tweepy
import datetime
import time
import json

count = 0
sleepTime = 600

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)


startDate = datetime.datetime(2020, 7, 9, 21, 29, 00)
endDate = datetime.datetime(2020, 7, 10, 21, 29, 00)
tweets = []


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        day = int(str(status.created_at)[8:10])
        month = int(str(status.created_at)[5:7])
        year = int(str(status.created_at)[0:4])
        hour = int(str(status.created_at)[11:13])
        min = int(str(status.created_at)[14:16])
        sec = int(str(status.created_at)[17:19])
        tweetDate = datetime.datetime(year, month, day, hour, min, sec)
        global count
        if tweetDate < endDate and tweetDate >= startDate:
            print(str(tweetDate)+status.text)
            with open('LamaAlherbish_tweets.json', 'a') as json_file:
                json.dump(status._json, json_file, indent=4)
                json_file.close()
            count += 1
            print(count)
        else:
            return False

    def on_error(self, status):
        global sleepTime
        if status == 420:
            print('---------------------------------------')
            time.sleep(sleepTime)
            sleepTime = sleepTime * 2


api = tweepy.API(auth)
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth, listener=myStreamListener)
myStream.filter(languages=['ar'], locations=[35.49, 17.93, 54.86, 31.62],
                is_async=True)
