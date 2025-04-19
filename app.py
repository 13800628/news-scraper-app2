import streamlit as st
from scraper.yahoo import fetch_yahoo_news
from scraper.nhk import fetch_nhk_news
import time

def fetch_news_with_retry(fetch_func, keyword=None, retries=3, delay=2):
    """
    ニュースデータをリトライ付きで取得する関数。
    fetch_func: データ取得のための関数（YahooまたはNHK）
    keyword: 検索したいキーワード（オプション）
    retries: 最大リトライ回数
    delay: リトライの間隔（秒）
    """
    for attempt in range(retries):
        try:
            news_data = fetch_func(keyword)
            if news_data:  # データが存在すればそのまま返す
                return news_data
            else:
                st.warning(f"試行 {attempt+1}: データが空でした。再試行中...")
        except Exception as e:
            st.warning(f"試行 {attempt+1}: エラーが発生しました ({str(e)})。再試行中...")
        
        time.sleep(delay)  # リトライの間隔を設ける
    
    # リトライしても取得できなかった場合のデフォルトデータ
    st.error("ニュースデータの取得に失敗しました。デフォルトのニュースを表示します。")
    return [{"title": "最新ニュースが取得できませんでした。", "link": "#"}]  # 仮のデータ

def get_news_data(source, keyword=None):
    """
    ニュースデータを取得する関数。
    source: ニュースサイト (Yahoo, NHK)
    keyword: 検索したいキーワード (オプション)
    """
    if source == "Yahoo":
        return fetch_news_with_retry(fetch_yahoo_news, keyword)
    elif source == "NHK":
        return fetch_news_with_retry(fetch_nhk_news, keyword)
    else:
        return []

def display_news(news_data):
    """
    ニュースデータを表示する関数
    news_data: 取得したニュースデータ
    """
    if news_data:
        for article in news_data:
            st.write(f"**{article['title']}**")
            st.write(f"[リンクはこちら]({article['link']})")
            st.write("---")
    else:
        st.warning("該当するニュースはありませんでした。")

def main():
    st.title("ニューススクレイパー")
    menu = ["ニュースサイト選択", "キーワードで検索"]
    choice = st.sidebar.radio("メニューを選択してください", menu)

    if choice == "ニュースサイト選択":
        site = st.selectbox("ニュースサイトを選択", ["Yahoo", "NHK"])
        if st.button("最新ニュースを取得"):
            news_data = get_news_data(site)
            display_news(news_data)
        
    elif choice == "キーワードで検索":
        keyword = st.text_input("検索したいキーワードを入力してください")
        if st.button("検索"):
            news_data = get_news_data("Yahoo", keyword) + get_news_data("NHK", keyword)
            display_news(news_data)

if __name__ == "__main__":
    main()