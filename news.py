import requests
import xml.etree.ElementTree as ET

RSS_FEED_URL = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"
def loadRSS():
    resp = requests.get(RSS_FEED_URL)
    return resp.content
def parseXML(rss):
    root = ET.fromstring(rss)
    newsitems = []
    for item in root.findall('./channel/item'):
        news = {}
        for child in item:
            if child.tag == '{https://rss.app/rss-feed?topicId=google}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
        newsitems.append(news)
    return newsitems
def  topstories():
    rss = loadRSS()


    newsitems = parseXML(rss)
    return newsitems
