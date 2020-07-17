import requests
from bs4 import BeautifulSoup

def liberal_times_crawler(url):
    headers = []
    news_url = []
    article = []
    time_dt = []

    for page_num in range(1,122):
        res_news = requests.get(url + repr(page_num))
        newslist_soup = BeautifulSoup(res_news.text, 'lxml')

        for newslist in newslist_soup.find_all('div', class_= 'whitecon'):
            li_label = newslist.find_all('li')

        # 新聞標題
        for t in li_label:
            headers.append(t.find('a').text)

        # 新聞連結
        url_sect = [t.find('a') for t in li_label]
        for t in url_sect:
            news_url.append(t.get('href'))

        # 新聞abstract
        p = [p.find('p') for p in li_label]
        for content in p:
            article.append(content.text)

        # 時間
        for t in li_label:
            time_dt.append(t.find('span').text for t in li_label)

        time.sleep(3)

    return headers, news_url, article, time_dt