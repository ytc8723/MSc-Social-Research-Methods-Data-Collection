from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
import pandas as pd
import time
import re


# 設置一定的點擊次數


def apple_crawler(url):
    """Collect news articles and links from
    Apple Daily ajax site using selenium"""

    browser = webdriver.Chrome('/Users/garday/Downloads/chromedriver')
    browser.get(url)

    i = 0
    for i in range(5):  # 設置點擊5次
        browser.find_element_by_id('moreButton').click()
        time.sleep(5)
        soup = BeautifulSoup(browser.page_source, 'lxml')

    # 取得新聞標題
    title = soup.find_all('div', class_='content')  # locate搜索結果位置
    headers = [t.find('a').text for t in title]
    headers = [' '.join(t.strip()) for t in headers]

    # 取得新聞連結
    urlsource = [t.find('a') for t in title]
    news_url = []
    for t in urlsource:
        news_url.append(t.get('href'))

    # 取得新聞內文
    ptag = [p.fine('p') for p in title]
    article = []
    for content in ptag:
        article.append(content.text)

    # 取得發布時間
    time = [t.find('time') for t in title]
    time_dt = []
    for i in time:
        time_dt.append(datetime.strptime(i, '%Y%m%d'))

    df = pd.DataFrame(
        {
            'titles': headers,
            'links': news_url,
            'content': article,
            'time': time_dt,
        })

    df.to_csv('/Users/garday/Documents/MY499/Data Collection/Data/馬英九_2012news.csv', encoding='utf_8_sig', index=None)

    return df
