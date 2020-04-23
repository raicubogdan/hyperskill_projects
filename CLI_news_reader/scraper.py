import requests
import bs4
from models.article import Article

res = requests.get('https://hotnews.ro')

soup = bs4.BeautifulSoup(res.content, 'lxml')

articles = soup.select('div.articol_lead_full')

news = []

for article in articles:
    # Getting link
    h2_tag = article.select('h2')
    link = h2_tag[0].find('a').get('href')

    # Getiing title
    title = h2_tag[0].find('a').get('title')

    # Geting descr
    lead = article.select('div.lead')
    descr = lead[0].text

    # Populates the news list with Article objects
    if link and title and descr is not None:
        news.append(Article(title, descr, link))
