import requests
# response=requests.get("https://www.google.com")
# print(response.text)
url="https://stackoverflow.com/questions/16694907/download-a-large-file-in-python-with-requests"
res=requests.get(url)

from bs4 import BeautifulSoup
soup=BeautifulSoup(res.text,"html.parser")
for li in soup.find_all("li"):
    print(li.text)
# print(soup.prettify())