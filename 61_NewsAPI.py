import requests
import json
import apikey
query=input("What type of news are you intrested in?\n")
url=f"https://newsapi.org/v2/everything?q={query}&from=2026-06-09&sortBy=publishedAt&apiKey={apikey.api}"
response=requests.get(url)
news=json.loads(response.text)
# print(news,type(news))


for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("="*70)
    