from bs4 import BeautifulSoup

class AnimePage:
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
    
    def getGenre(self, soup):
        genre = []
        for g in soup.find('li', {'class': 'right'}).find_all('a'):
            genre.append(g.text)
        return genre
    
    def getEpisodes(self, soup):
        episodes = []
        players = []
        for e in soup.find_all('div', {'class': 'player_box'}):
            player = e.get('id').replace('content_', '');
            tryparsing = soup.find('div', {'id': player})
            if tryparsing:
                meth = soup.find('div', {'id': player})['class'][0];
                id = e.text
                players.append({'player': player, 'link': self.getLecteur(id, meth)})
        for e in soup.find_all('div', {'class': 'button_box'}):
            id = e.get('id').replace('buttons_', '');
            link = []
            for data in e.find_all('div'):
                for p in players:
                    if p['player'] == data.get('id'):
                        link.append(p['link'])
            episodes.append({'id': id, 'link': link})
        return episodes

    def  getLecteur(self, id, meth):
        if meth == "new_player_myvi":
            return 'https://myvi.ru/player/embed/html/'+id

        elif meth == "new_player_vip":
            return id

        elif meth == "new_player_gtv":
            return "https://iframedream.com/embed/"+id+".html"

        elif meth == "new_player_mp4":
            return "https://www.mp4upload.com/embed-"+id+".html"

        elif meth == "new_player_uqload":
            return "https://uqload.com/embed-"+id+".html"

        elif meth == "new_player_vidfast":
            return "http://vosmanga.tk/watch/"+id

        elif meth == "new_player_verystream":
            return "https://verystream.com/e/"+id

        elif meth == "new_player_rapids":
            return "https://rapidstream.co/embed-"+id+".html"

        elif meth == "new_player_cloudvideo":
            return "https://cloudvideo.tv/embed-"+id+".html"

        elif meth == "new_player_mytv":
            return "https://www.myvi.xyz/embed/"+id

        elif meth == "new_player_uptostream":
            return "https://uptostream.com/iframe/"+id

        elif meth == "new_player_fembed":
            return "https://www.fembed.com/v/"+id+".html"

        elif meth == "new_player_rapidvideo":
            return "https://www.rapidvideo.com/e/"+id

        elif meth == "new_player_tune":
            return "https://tune.pk/player/embed_player.php?vid="+id

        elif meth == "new_player_sibnet":
            return "https://video.sibnet.ru/shell.php?videoid="+id

        elif meth == "new_player_netu":
            return "https://waaw.tv/watch_video.php?v="+id

        elif meth == "new_player_rutube":
            return "https://rutube.ru/play/embed/"+id

        elif meth == "new_player_yandex":
            return id

        elif meth == "new_player_ok":
            return 'https://www.ok.ru/videoembed/'+id

        elif meth == "new_player_vid":
            return id

        elif meth == "new_player_cloudy":
            return id

        elif meth == "new_player_google":
            return 'https://drive.google.com/open?id='+id

        elif meth == "new_player_youtube":
            return id

        elif meth == "new_player_moevideo":
            return id

        elif meth == "new_player_mail":
            return "https://videoapi.my.mail.ru/videos/embed/mail/"+id

        elif meth == "new_player_mail2":
            return "https://my.mail.ru/video/embed/"+id

        elif meth == "new_player_vk2":
            return id

        elif meth == "new_player_dailymotion":
            return "https://dailymotion.com/embed/video/"+id

        elif meth == "new_player_openload":
            return "https://openload.co/embed/"+id

        elif meth == "new_player_kaztube":
            return "https://kaztube.kz/video/embed/"+id

        else:
            return id

class SearchPage:
    def __init__(self):
        self.url = 'https://vostfree.tv'
    