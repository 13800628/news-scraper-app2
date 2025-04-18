import requests
from bs4 import BeautifulSoup

def fetch_yahoo_news():
    url = "https://news.yahoo.co.jp/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    news_items = []
    for item in soup.select('a[href^="https://news.yahoo.co.jp/articles/"]'):
        title = item.get_text(strip=True)
        link = item.get("href")
        if title and link:
            news_items.append({"Title": title, "Link": link})

    return news_items