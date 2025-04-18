# News Scraper App

Yahoo!ニュース & NHKニュースから記事を取得し、キーワード検索やサイト別に表示するStreamlit製のWebアプリです。

## 機能

- ニュースサイトを選択（Yahoo! / NHK）
- キーワード検索
- シンプルで直感的なUI（Streamlit使用）

## 使用技術

- Python
- Streamlit
- BeautifulSoup4
- Requests
- Pandas

## セットアップ

```bash
git clone https://github.com/yourname/news-scraper-app.git
cd news-scraper-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

