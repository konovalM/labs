import requests
from bs4 import BeautifulSoup
from termcolor import colored, cprint


def extract_news(parser):
    """ Extract news from a given web page """
    news_list = []

    # PUT YOUR CODE HERE
    try:
        page = parser.table.findAll('table')[1]
    except Exception:
        return 'error'
    try:
        for i in range(30):
            news = dict()
            title = page.findAll('tr')[3*i].findAll('td')[2].a.text
            try:
                link = page.findAll('tr')[3*i].findAll('td')[2].span.span.text
            except AttributeError:
                link = 'no_url =('
            points = page.findAll('tr')[3*i+1].findAll('td')[1].span.text
            points_last = ''
            for j in points:
                if not j.isdigit():
                    break
                points_last += j
            author = page.findAll('tr')[3*i+1].findAll('td')[1].a.text
            comments = page.findAll('tr')[3*i+1].findAll('td')[1].findAll('a')[-1].text
            comments_last = ''
            if comments == 'discuss':
                comments_last = 0
            else:
                for j in comments:
                    if not j.isdigit():
                        break
                    comments_last += j
            news = {'author':author, 'comments':int(comments_last), 'points':int(points_last), 'title':title, 'url':link}
            news_list.append(news)
            
    except Exception:
        print('На странице нет 30 новостей')

    return news_list


def extract_next_page(parser):
    """ Extract next page URL """
    # PUT YOUR CODE HERE
    page = parser.table.findAll('table')[1]
    try:
        additional_link = page.findAll('tr')[-1].findAll('td')[1].a['href']
        return additional_link
    except Exception:
        return 'newest'


def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        if news_list == 'error':
            print(colored('Нет доступа к следующей странице!', 'red', attrs=['underline']))
            break
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        #print ("https://news.ycombinator.com/" + next_page)
        news.extend(news_list)
        n_pages -= 1
    return news

'''TEST'''
test = get_news("https://news.ycombinator.com/newest", 5)


