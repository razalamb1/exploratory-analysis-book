import boto3
import nltk
from pathlib import Path

client = boto3.client('comprehend')
!wget https://gutenberg.org/cache/epub/4367/pg4367.txt
grant_book = Path('pg4367.txt').read_text()
 
response = client.detect_sentiment(Text=grant_book, LanguageCode = 'en')
