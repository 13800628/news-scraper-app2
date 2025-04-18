import requests
from bs4 import BeautifulSoup

def fetch_yahoo_news(keyword=None):
    """
    Yahooニュースをスクレイピングして取得する関数
    keyword: 検索したいキーワード (オプション)
    """
    url = f"https://news.yahoo.co.jp/" if not keyword else f"https://news.yahoo.co.jp/search?p={keyword}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        
        articles = []
        for item in soup.find_all('li', class_='newsFeed_item'):
            title = item.find('a').get_text()
            link = item.find('a')['href']
            articles.append({'title': title, 'link': link})
        
        return articles
    
    except requests.RequestException as e:
        print(f"Error fetching Yahoo news: {e}")
        return []