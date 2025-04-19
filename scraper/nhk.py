import requests
from bs4 import BeautifulSoup

def fetch_nhk_news(keyword=None):
    url = f"https://www3.nhk.or.jp/news/" if not keyword else f"https://www3.nhk.or.jp/news/search/?q={keyword}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        
        articles = []
        if keyword:
            for item in soup.select("div.searchResultItem"):  # 検索結果
                a_tag = item.find('a')
                if a_tag:
                    title = a_tag.get_text(strip=True)
                    link = a_tag['href']
                    articles.append({'title': title, 'link': f"https://www3.nhk.or.jp{link}"})
        else:
            for item in soup.select("div.content--list-item > a"):  # トップページ
                title = item.get_text(strip=True)
                link = item['href']
                articles.append({'title': title, 'link': f"https://www3.nhk.or.jp{link}"})

        return articles

    except requests.RequestException as e:
        print(f"Error fetching NHK news: {e}")
        return []