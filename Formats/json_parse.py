import json


def json_news():
    with open('newsafr.json') as file:
        data = json.load(file)
    news_data = data['rss']['channel']['items']
    return news_data


def news_list(news_data):
    news_list = []
    for news in news_data:
        news_list.append(news['description'])
    return news_list


def sorted_news(news_list):
    split_list = []
    overall_news = []
    for news in news_list:
        split_list.append(news.split())
    for split in split_list:
        for words in split:
            if len(words) > 6:
                overall_news.append(words)
    sorted_list = sorted(overall_news, key=overall_news.count, reverse=True)
    uniq_list = sorted(set(sorted_list), key=lambda temp: sorted_list.index(temp))
    top_news = uniq_list[:10]
    return top_news


news_data = json_news()
news_list = news_list(news_data)
top_news = sorted_news(news_list)

print(top_news)

