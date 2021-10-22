from vostfree import VostFree

def getAnimeById(id):
    anime = {}
    url = 'https://vostfree.tv/' + str(id) + '-ddl-streaming-1fichier-uptobox.html'
    vost = VostFree()
    soup = vost.getSoup(url)
    anime['title'] = vost.getTitle(soup)
    anime['description'] = vost.getDesc(soup)
    anime['image'] = vost.getMainImg(soup)
    anime['nbepisode'] = vost.getNbEpisodes(soup)
    return anime;