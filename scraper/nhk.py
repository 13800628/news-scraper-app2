# scraper/nhk.py
import requests
from bs4 import BeautifulSoup

def fetch_nhk_news():
    url = "https://www3.nhk.or.jp/news/"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    news_items = []

    for item in soup.select(".content--list li a"):  # セレクタは後で調整可能
        title = item.get_text(strip=True)
        link = item.get("href")
        if title and link:
            # フルURLでなければ付け足す
            if link.startswith("/"):
                link = "https://www3.nhk.or.jp" + link
            news_items.append({"Title": title, "Link": link})
    
    return news_items