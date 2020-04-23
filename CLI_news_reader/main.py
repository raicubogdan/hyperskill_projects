# CLI News reader. Grabs news from https://hotnews.ro
# and displays them in terminal. Shows headlines,
# descriptions and articles content.

from News_grab import News_grab


print('''
---CLI News Reader---

The article list updates every time you filter
or display the full news list. Description and content
will be read from the previous displayed list of articles
(filtered or all).

Use Shift + PgUp/PgDn or mouse wheel to navigate through the lists.
''')

news_grab = News_grab()
while True:
    option = str(input('''Menu:

1. List all headlines
2. Filter articles by keyword in headline
3. Read article description
4. Read article
5. Exit
>> '''))

    if option == '1':
        news_grab.show_titles()

    elif option == '2':
        keyword = input('Type keyword here: ')
        news_grab.filter_titles(keyword)

    elif option == '3': 
        try:
            idx = int(input(f'Type article number (1 - {len(news_grab.curr)}) : '))
            news_grab.read_descr(idx)
        except Exception:
            print('\nInvalid input, try again.')

    elif option == '4':
        try:
            idx = int(input(f'Type article number (1 - {len(news_grab.curr)}) : '))
            news_grab.read_article(idx)
        except Exception:
            print('\nInvalid input, try again.')

    elif option == '5':
        exit()

    else:
        print('\nInvalid input.\n')
