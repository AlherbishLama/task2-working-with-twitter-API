import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


df = pd.read_json(r'LamaAlherbish_tweets.json')
df = df[['created_at', 'text']]
df['created_at'] = pd.DatetimeIndex(df['created_at'])
df = df.groupby(pd.Grouper(key='created_at',freq='60Min', base=29)).count()

df = df.rename(columns={'text': 'number_of_tweets'})
print(df)
print('-----------------------------------')
df.index = (df.index).astype(str)
df['time'] = df.index.str.slice(11, 13)
print(df)

ax = plt.gca()

df.plot(x ='time', y='number_of_tweets', kind='line', ax=ax)
plt.title('Number of tweets per hour', fontsize=12)
plt.xlabel('Hour', fontsize=10)
plt.ylabel('Number of tweets', fontsize=10)
plt.savefig('LamaAlherbish_lineChart.png')
