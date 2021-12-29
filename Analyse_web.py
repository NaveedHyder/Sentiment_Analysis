from textblob import TextBlob
from newspaper import Article

url = 'https://www.ndtv.com/india-news/jds-leader-ex-pm-hd-deve-gowda-as-monsoon-session-ends-early-amid-protests-i-feel-sad-2508694'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity  # -1 to 1
print(sentiment)
