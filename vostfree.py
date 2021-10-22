from bs4 import BeautifulSoup


class VostFree:
    def __init__(self):
        self.url = 'https://vostfree.tv'

    def getSoup(self, url):
        return BeautifulSoup(self.getHtml(url), 'html.parser')

    def getHtml(self, url):
        import requests
        return requests.get(url).text

    def getTitle(self, soup):
        return soup.find('h1').text
    
    def getDesc(self, soup):
        return soup.find('meta', {'name': 'description'})['content']

    def getMainImg(self, soup):
        return self.url + soup.find('img', {'width': '200'})['src']
    
    def getNbEpisodes(self, soup):
        return int(soup.find('div', {'class': 'year'}).text.replace('Episode ', ''))

__init__ = VostFree()