import urllib.parse

import feedparser
import requests
from bs4 import BeautifulSoup as bs4


def openfile(filename):
    fp = open(filename)
    list_of_lines = fp.readlines()
    fp.close()
    return list_of_lines


def find_feed(site):
    raw = requests.get(site).text
    result = []
    possible_feeds = []
    html = bs4(raw, features="html.parser")
    feed_urls = html.findAll("link", rel="alternate")
    for f in feed_urls:
        t = f.get("type", None)
        if t:
            if "rss" in t or "xml" in t:
                href = f.get("href", None)
                if href:
                    possible_feeds.append(href)
    parsed_url = urllib.parse.urlparse(site)
    base = parsed_url.scheme + "://" + parsed_url.hostname
    atags = html.findAll("a")
    for a in atags:
        href = a.get("href", None)
        if href:
            if "xml" in href or "rss" in href or "feed" in href:
                possible_feeds.append(base + href)
    for url in list(set(possible_feeds)):
        f = feedparser.parse(url)
        if len(f.entries) > 0:
            if url not in result:
                result.append(url)
    return result


def main():
    # Values for file path.
    path = 'webpages.txt'

    # Get website list
    names = openfile(path)
    for x in range(len(names)):
        try:
            feed = find_feed(names[x])
            if feed:
                print(feed)
        except Exception as err:
            print(err)
        finally:
            pass


if __name__ == "__main__":
    main()
