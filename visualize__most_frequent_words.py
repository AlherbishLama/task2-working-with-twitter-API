#coding=utf-8
import json
import re
from collections import Counter
from itertools import chain
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from arabic_reshaper import arabic_reshaper
from bidi.algorithm import get_display
import itertools
from stop_words import get_stop_words
from nltk.tokenize import RegexpTokenizer
from mosestokenizer import *


tweets_data = []
tweets_data2 = []
twenty_most_commom_words_with_frequency = []
twenty_most_commom_words = []
stop_words = set(get_stop_words('arabic'))


characters = ['!', '@', '$', '%', '^', '&', '*', '/', '{', '}', '[', ']',
              '\'', '+', '=', '>', '<', '?', '|', '~', ':', ';', ',', '.',
              '-', '(', ')', '\"', '\\', '،', '…', '‐', '؟']

arabic_words = ['يا', 'الي', 'لو', 'لي','من', 'اله', 'كل', 'ما', 'ولا','صح', 'لا'
                ,'له', 'في', 'انا', 'ال', 'و', 'شي', 'أن', 'وال', 'لك', 'بس', 'انت'
                ,'على', 'بعد','ان', 'عن', 'مع', 'هذا', 'ه','فيه', 'كان', 'هو',
                'اذا', 'واله', 'الا','حتى', 'وش', 'عليه', 'عليك', 'او', 'كيف', 'إلا',
                'مو', 'فيها', 'الى', 'فيها', 'لم', 'قبل', 'شيء', 'عشان', 'هل',
                'اي', 'اني', 'غير', 'امين', 'كنت', 'وانا', 'إلى', 'هذه', 'الذي',
                'باله', 'لها', 'قال', 'هي', 'تم', 'لكن', 'التي', 'إن', 'ومن',
                'أو', 'ع', 'يعني', 'لنا', 'انه', 'بين', 'م']


def clean_Text(str):
    # Remove @usernames from tweet text
    text1 = re.sub(r'@\S+', '', str)

    # Remove URLs
    text2 = re.sub(r'http\S+', '', text1)

    text2 = re.sub(r'#(\w+)', '', text2)

    emoji_pattern = re.compile("["u"\U0001F600-\U0001F64F"  # emoticons
                                  u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                  u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                  u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                  u"\U00002702-\U000027B0"
                                  u"\U000024C2-\U0001F251"
                                  "]+", flags=re.UNICODE)
    text2 = emoji_pattern.sub(r'', text2)


    # Remove characters
    for char in characters:
        text2 = text2.replace(char, "")

    # Replace multi Spaces with one space
    text2 = re.sub(' +', ' ', text2)
    # Replace multi Tabs with one space
    text2 = re.sub('\t +', ' ', text2)
    # Replace multi Newlines with one space
    text2 = re.sub('\n +', ' ', text2)

    # Remove duplicated characters
    text2 = ''.join(char for char, _ in itertools.groupby(text2))

    text2 = text2.split()

    result = [word for word in text2 if word not in arabic_words]

    final_result = ' '.join(result)

    return final_result


with open('LamaAlherbish_tweets.json') as f:
    print('hh')
    data_file = json.load(f)
    # print(data_file)
    for i in data_file:
        cleaned_text = clean_Text(str=i['text'])
        tweets_data.append(cleaned_text.split())
    tweets_data2 = list(chain.from_iterable(tweets_data))
    twenty_most_commom_words_with_frequency = Counter(tweets_data2).most_common(20)
    for word in twenty_most_commom_words_with_frequency:
        print(word[0])
        twenty_most_commom_words.append(word[0])


# # convert list to string and generate
unique_string = (" ").join(twenty_most_commom_words)
reshaped_texts = arabic_reshaper.reshape(unique_string)
reshaped_texts = get_display(reshaped_texts)
wordcloud = WordCloud(font_path='Fonts/Supplemental/Damascus.ttc', width=700, height=300, background_color="white").generate(reshaped_texts)
plt.axis('off')
plt.imshow(wordcloud, interpolation='bilinear')
plt.savefig('LamaAlherbish_wordCloud.png')
