import requests
from BeautifulSoup import BeautifulSoup
import BeautifulSoup as bs
from BeautifulSoup import BeautifulStoneSoup


REQUEST_TIMEOUT = 3


def crawl(url):
    response = requests.get(url, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    soup = BeautifulSoup(response.content)
    return soup

def filter_keyword_soolve(tag):
    return tag.parent is not None and tag.parent.parent is not None and tag.parent.parent.get('class') == 'correction'


def parse_and_get_top(soup):
    return map(str, soup.findAll(text=filter_keyword_soolve))


def craw_and_parse(url, domain):
    return parse_and_get_top(crawl(url))


def main():
    # soup = crawl('http://soovle.com/top/')
    # top_words = parse_and_get_top(soup)
    # for word in top_words:
    #     print word
    response = requests.get('https://trends.google.com/trends/hottrends/atom/hourly')
    soup = BeautifulSoup(response.content)
    c = soup.findAll(text=lambda x:isinstance(x, bs.CData))
    # print ''.join(c)
    c = '<html>' + ''.join(c) + '</html>'
    ps = BeautifulSoup(c)
    links = ps.findAll('a')
    print map(lambda x:str(x.string), links)
if '__name__' == main():
    main()
