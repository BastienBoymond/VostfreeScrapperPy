from VostfreeScrapperPy.vostfree import AnimePage

def getAnimeById(id):
    anime = {}
    url = 'https://vostfree.tv/' + str(id) + '-ddl-streaming-1fichier-uptobox.html'
    vost = AnimePage()
    soup = vost.getSoup(url)
    anime['url'] = url
    anime['title'] = vost.getTitle(soup)
    anime['description'] = vost.getDesc(soup)
    anime['image'] = vost.getMainImg(soup)
    anime['nbepisodes'] = vost.getNbEpisodes(soup)
    anime['genres'] = vost.getGenre(soup)
    anime['episodes'] = vost.getEpisodes(soup)
    return anime;

def getAnimeByUrl(url):
    anime = {}
    vost = AnimePage()
    soup = vost.getSoup(url)
    anime['url'] = url
    anime['title'] = vost.getTitle(soup)
    anime['description'] = vost.getDesc(soup)
    anime['image'] = vost.getMainImg(soup)
    anime['nbepisodes'] = vost.getNbEpisodes(soup)
    anime['genres'] = vost.getGenre(soup)
    anime['episodes'] = vost.getEpisodes(soup)
    return anime;