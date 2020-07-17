## import packages
import time
from selenium import webdriver
from selenium.webdriver.common.keys import keys
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

def load_web_page(url):
    '''Load the url to load data through ajax'''

    browser = webdriver.Chrome('/Users/garday/Downloads/chromedriver')
    browser.get(url)

    i = 0
    for i in range(100):
        browser.find_element_by_id('moreButton').click()
        time.sleep(3)
        soup = BeautifulSoup(browser.page_source, 'lxml')

    return

def extract(soup):

    title = soup.find_all('div', class_ = 'content')

    headers = [t.find('a').text for t in title]

    test = [t.find('a') for t in title]
    news_url = []
    for t in test:
        news_url.append(t.get('href'))

    p = [p.find('p') for p in title]
    article = []
    for content in p:
        article.append(content.text)

    time_text = [t.find('time').text for t in title]
    time_dt = []
    for i in time_text:
        time_dt.append(datetime.strptime(i, '%Y%m%d'))

    return headers, news_url, article, time_dt

def media_label(headers):
    media = []
    for i in len(range(headers)):
        media.append('Apple Daily')
    return media

def news_dataframe(headers, news_url, abstract, time_dt):
    '''Save the headers and url into a pandas data frame, and
    then save it into csv file'''

    df = pd.DataFrame(
    {
        'headers': headers,
        'news_url': news_url,
        'Content' : abstract,
        'Time' : time_dt
    }, index = None)
    return df

news_dataframe = news_dataframe(headers, news_url)
type(news_dataframe)
news_dataframe.to_csv('/Users/garday/Documents/MY499/Data Collection/Data/馬英九news_2012.csv', \
                      encoding = 'utf_8_sig', index = None)


def china_times_webcrawler(url):
    headers = []
    news_url = []
    time_dt = []
    time_nw = []

    for page_num in range(135, 342):
        res_news = requests.get(url + repr(page_num) + '&chdtv')
        newslist_soup = BeautifulSoup(res_news.text, 'lxml')

        for newslist in newslist_soup.find_all('div', class_ = 'item-list article-list'):
            title_sect = newslist.find_all('h3')

        for t in title_sect:
            headers.append(t.find('a').text)

        url_sect = [t.find('a') for t in title_sect]
        for t in url_sect:
            news_url.append(t.get('href'))

        for i in newslist_soup.find_all('div', class_ = 'item-list article-list'):
            time_test = i.find_all('div', class_ = 'meta-info')
        for t in time_test:
            time_dt.append(t.find('time').text)
        for t in time_dt:
            time_new.append(i.replace(i[:5], ''))

        time.sleep(2)

    media = []
    for i in range(len(headers)):
        media.append('China Times')

    return headers, news_url, time_new, media
