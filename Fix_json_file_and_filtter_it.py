import json

tweets_objects = []

# add comma between json objects

with open("LamaAlherbish_tweets.json", "r+") as f:
    old = f.read()
    f.seek(0)  # rewind
    f.write(old.replace('}{', '},{'))


# remove all the tweets objects that wasn't created in saudi arabia

with open('LamaAlherbish_tweets.json') as q:
    data_file = json.load(q)
    for i in data_file:
        if i['place']is not None and i['place']['country_code']is not None:
            if i['place']['country_code'] == 'SA':
                tweets_objects.append(i)
        else:
            print('nahhhhh')

with open('LamaAlherbish_tweets.json', 'w') as e:
    for s in tweets_objects:
        json.dump(s, e, indent=4)
