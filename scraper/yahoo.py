import requests
from bs4 import BeautifulSoup

def fetch_yahoo_news(keyword=None):
    url = f"https://news.yahoo.co.jp/" if not keyword else f"https://news.yahoo.co.jp/search?p={keyword}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        
        articles = []
        # Yahooのトップページと検索結果の構造が異なるため分岐
        if keyword:
            for item in soup.select("div.sw-Card__contents"):  # 検索結果
                title_tag = item.find('a')
                if title_tag:
                    title = title_tag.get_text(strip=True)
                    link = title_tag['href']
                    articles.append({'title': title, 'link': link})
        else:
            for item in soup.select("a.newsFeed_item_link"):  # トップページ
                title = item.get_text(strip=True)
                link = item['href']
                articles.append({'title': title, 'link': link})

        return articles

    except requests.RequestException as e:
        print(f"Error fetching Yahoo news: {e}")
        return []