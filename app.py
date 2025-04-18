import streamlit as st
from scraper.yahoo import fetch_yahoo_news
from scraper.nhk import fetch_nhk_news

# ニュースサイト選択
st.title('ニューススクレイピング')
option = st.selectbox("選択してください", ["ニュースサイトを選んで全てを表示", "キーワードで検索"])

if option == "ニュースサイトを選んで全てを表示":
    site_option = st.selectbox("ニュースサイトを選んでください", ["Yahoo", "NHK"])

    # ユーザーが選んだサイトに基づいてニュースを取得する
    if site_option == "Yahoo":
        st.write("Yahoo!ニュースを選択しました")
        news_data = fetch_yahoo_news()
        st.write("全ての記事を表示しています:")
        for news in news_data:
            st.write(f"- {news['Title']} : {news['Link']}")

    elif site_option == "NHK":
        st.write("NHKニュースを選択しました")
        news_data = fetch_nhk_news()
        st.write("全ての記事を表示しています:")
        for news in news_data:
            st.write(f"- {news['Title']} : {news['Link']}")

elif option == "キーワードで検索":
    keyword = st.text_input("検索するキーワードを入力してください")

    if keyword:
        # Yahooでの検索
        yahoo_news_data = fetch_yahoo_news()
        filtered_yahoo = [news for news in yahoo_news_data if keyword.lower() in news['Title'].lower()]
        
        # NHKでの検索
        nhk_news_data = fetch_nhk_news()
        filtered_nhk = [news for news in nhk_news_data if keyword.lower() in news['Title'].lower()]

        if filtered_yahoo or filtered_nhk:
            st.write("キーワードにマッチする記事:")

            # Yahooの結果を表示
            if filtered_yahoo:
                st.write("Yahoo!ニュース:")
                for news in filtered_yahoo:
                    st.write(f"- {news['Title']} : {news['Link']}")

            # NHKの結果を表示
            if filtered_nhk:
                st.write("NHKニュース:")
                for news in filtered_nhk:
                    st.write(f"- {news['Title']} : {news['Link']}")

        else:
            st.write("キーワードにマッチする記事は見つかりませんでした。")