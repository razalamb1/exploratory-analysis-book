import boto3
import nltk
from pathlib import Path
import math
import pandas as pd

client = boto3.client('comprehend')
grant_book = Path('pg4367.txt').read_text()
grant_book = grant_book[0:200000]

length = len(grant_book)
iterations = math.ceil(length/4000)
sentiment = pd.DataFrame(columns = ['Count', 'Sentiment', 'Positive', 'Negative', 'Neutral', 'Mixed'])

for i in range(iterations):
    lower_bound = i*4000
    upper_bound = (i+1)*4000 + 1
    temp_text = grant_book[lower_bound:upper_bound]
    response = client.detect_sentiment(Text=temp_text, LanguageCode = 'en')
    score = response['SentimentScore']
    sentiment = sentiment.append({'Count': i, 'Sentiment': response['Sentiment'], 'Positive': score['Positive'], 'Negative': score['Negative'], 'Neutral': score['Neutral'], 'Mixed':score['Mixed']}, ignore_index = True)
    pass


print(sentiment)