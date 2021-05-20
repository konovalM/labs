from bottle import debug, redirect, request, route, run, template

from bayes import NaiveBayesClassifier
from db import News, session
from scraputils import get_news


@route("/news")
def news_list():
    debug(True)
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template("news_template", rows=rows)


@route("/add_label/")
def add_label():
    label = request.query["label"]
    #print(request.query)
    id = request.query["id"]
    #print(label)
    #print(id)
    print(label, id)
    s = session()
    page = s.query(News).get(id)
    print(page.label)
    page.label = label
    print(page.label)
    s.add(page)
    s.commit()
    print(page.title)
    redirect("/news")


@route("/update")
def update_news():
    s = session()
    test = get_news("https://news.ycombinator.com/newest", 2)
    for i in range(len(test)):
        if len(s.query(News).filter(News.title == test[i]['title']).filter(News.author == test[i]['author']).all()) == 0:
            news = News(title=str(test[i]['title']), 
                    author=str(test[i]['author']),
                    url=str(test[i]['url']),
                    comments=int(test[i]['comments']),
                    points=int(test[i]['points']))
            s.add(news)
            s.commit()
    redirect("/news")


@route("/classify")
def classify_news():
    # PUT YOUR CODE HERE
    pass


if __name__ == "__main__":
    run(reloader=True)
    