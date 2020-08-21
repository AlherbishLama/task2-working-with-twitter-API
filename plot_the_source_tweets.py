import json
import matplotlib.pyplot as plt
import numpy as np

android = 0
iphone = 0
webApp = 0

with open('LamaAlherbish_tweets.json') as f:
    data_file = json.load(f)
    for i in data_file:
        if 'iPhone' in i['source']:
            iphone += 1
        elif 'Android' in i['source']:
            android += 1
        elif 'Web App' in i['source']:
            webApp += 1
typeOfDevice = ('iPhone', 'Android', 'Web App')
y_pos = np.arange(len(typeOfDevice))
frequency = [iphone, android, webApp]
plt.bar(y_pos, frequency, align='center', alpha=0.5)
plt.xticks(y_pos, typeOfDevice)
plt.ylabel('frequency')
plt.title('frequency of different types of the client applications')

plt.savefig('LamaAlherbish_barChart.png')
