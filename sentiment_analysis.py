import boto3
from pathlib import Path
import math
import pandas as pd
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

client = boto3.client('comprehend')
grant_book = Path('pg4367.txt').read_text()
chapters = re.split(r"\n{4,5}CHAPTER [IXV]+\.", grant_book)



def chapter_sentiment(chapter):
    length = len(chapter)
    iterations = math.ceil(length/4000)
    sentiment = pd.DataFrame(columns =  ['Length','Positive', 'Negative', 'Neutral', 'Mixed'])
    for i in range(iterations):
        lower_bound = i*4000
        upper_bound = (i+1)*4000 + 1
        temp_text = chapter[lower_bound:upper_bound]
        num = len(temp_text)
        response = client.detect_sentiment(Text=temp_text, LanguageCode = 'en')
        score = response['SentimentScore']
        score['Length'] = num
        sentiment = sentiment.append(score, ignore_index = True)
        pass
    sentiment.loc[:,'Length'] = sentiment.loc[:,'Length']/sentiment.loc[:,'Length'].sum()
    sentiment = sentiment.iloc[:,1:].multiply(sentiment.iloc[:,0], axis="index")
    sentiment = sentiment.sum(axis = 0)
    return sentiment.to_dict()
    

final = pd.DataFrame(columns =  ['Chapter','Positive', 'Negative', 'Neutral', 'Mixed'])
for i in range(len(chapters)):
    sentiment = chapter_sentiment(chapters[i])
    sentiment['Chapter'] = f'{i}'
    final = final.append(sentiment, ignore_index=True)
    pass

plt.plot(final['Chapter'], final['Positive'], label = "Positive")
plt.plot(final['Chapter'], final['Negative'], label = "Negative")
plt.plot(final['Chapter'], final['Neutral'], label = "Neutral")
plt.plot(final['Chapter'], final['Mixed'], label = "Mixed")
plt.xlabel("Chapter")
plt.ylabel("Proportion")
plt.title("Sentiment Analysis by Chapter")
plt.legend()
plt.savefig('display.png')