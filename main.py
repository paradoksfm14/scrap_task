import requests
import bs4

HEADERS = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Accept-Language' : 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control' : 'max-age=0',
    'Connection' : 'keep-alive',
    'Cookie' : '_ym_d=1659031932; _ym_uid=1659031932229405972; hl=ru; fl=ru; _ga=GA1.2.946146414.1659031933; habr_web_home_feed=/all/; _ym_isad=2; _gid=GA1.2.1470921299.1665155697',
    'Host' : 'habr.com',
    'sec-ch-ua' : '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile' : '?0',
    'sec-ch-ua-platform' : "Windows",
    'Sec-Fetch-Dest' : 'document',
    'Sec-Fetch-Mode' : 'navigate',
    'Sec-Fetch-Site' : 'same-origin',
    'Sec-Fetch-User' : '?1',
    'Upgrade-Insecure-Requests' : '1',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 '
    }

responce = requests.get('https://habr.com/ru/all/', headers= HEADERS)
text = responce.text

KEYWORDS = {'дизайн', 'фото', 'web', 'python', 'интервью', 'Копирайт', 'Искусственный интеллект'}

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all(class_='tm-article-snippet')
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = {hub.find('a').text.strip() for hub in hubs}
    if hubs & KEYWORDS:
        data_tag_title = article.find('time')
        article_tag_a = article.find('h2').find('a')
        href = article_tag_a.attrs['href']
        url = 'https://habr.com' + href
        print(f'Дата: {data_tag_title.text}\nСтатья: {article_tag_a.text}\nСсылка: {url}\n')