import streamlit as st
from scraper.yahoo import fetch_yahoo_news
from scraper.nhk import fetch_nhk_news

def get_news_data(source, keyword=None):
    """
    ニュースデータを取得する関数。
    source: ニュースサイト (Yahoo, NHK)
    keyword: 検索したいキーワード (オプション)
    """
    if source == "Yahoo":
        return fetch_yahoo_news(keyword)
    elif source == "NHK":
        return fetch_nhk_news(keyword)
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