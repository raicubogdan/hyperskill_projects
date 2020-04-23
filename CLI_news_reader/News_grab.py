from scraper import news, requests, bs4


class News_grab:
    def __init__(self):
        self.curr = news

    def show_titles(self):
        self.curr = []
        for idx, article in enumerate(news):
            print(idx+1, article.title + '\n')
            self.curr.append(article)

    def filter_titles(self, keyword):
        titles = list(filter(lambda article: keyword in article.title, news))
        if len(titles) < 1:
            print('\nSorry, there are no titles containing your keyword.\n')
        else:
            self.curr = []
            for idx, article in enumerate(titles):
                print(idx+1, article.title + '\n')
                self.curr.append(article)

    def read_descr(self, idx):
        try:
                print(f'\n{self.curr[idx - 1].descr}\n')
        except Exception:
            print(f"\nArticle with number {idx} doesn't exist, try again.\n")

    def read_article(self, idx):
        art_cont = requests.get(self.curr[idx - 1].link)
        soup = bs4.BeautifulSoup(art_cont.text, 'lxml')
        content = soup.select('#articleContent')
        print('\n', content[0].text, '\n')
