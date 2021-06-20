import xml.etree.ElementTree as Tree


def xml_news():
    news_list = []
    parser = Tree.XMLParser(encoding="utf-8")
    tree = Tree.parse('newsafr.xml', parser)
    root = tree.getroot()
    description_list = root.findall('channel/item/description')
    for news in description_list:
        news_list.append(news.text)
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


news_list = xml_news()
top_news = sorted_news(news_list)

print(top_news)

