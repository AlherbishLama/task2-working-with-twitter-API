import json
import matplotlib.pyplot as plt


num_of_retweeted_tweets = 0
num_of_original_tweets = 0
total_num_of_tweets = 0

with open('LamaAlherbish_tweets.json') as f:
    data_file = json.load(f)
    for i in data_file:
        if 'RT' in i['text'] or i['retweeted'] is True:
            num_of_retweeted_tweets += 1
            total_num_of_tweets += 1
        elif i['retweeted'] is False and i['favorited'] is False:
            num_of_original_tweets += 1
            total_num_of_tweets += 1

persent_original = round((num_of_original_tweets/total_num_of_tweets)*100, 1)
persent_retweeted = round((num_of_retweeted_tweets/total_num_of_tweets)*100, 1)

labels = ['retweeted tweets  '+str(persent_retweeted), 'original tweets  '+str(persent_original)]
sizes = [persent_retweeted, persent_original]
inst = [str(persent_retweeted), str(persent_original)]
colors = ['lightskyblue', 'lightcoral']
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.savefig('LamaAlherbish_pieChart.png')
