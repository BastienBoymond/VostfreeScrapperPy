from VostfreeScrapperPy.vostfree import Page

def getLastNewsPage(page):
    anime= {}
    url =  'https://vostfree.tv/lastnews/page/' + str(page)
    vost = Page()
    soup = vost.getSoup(url)
    anime['url'] = url
    anime['page'] = page
    anime['animes'] = vost.getAnimes(soup)
    return anime

def getAnimesByGenreAndPage(genre, page):
    anime= {}
    url =  'https://vostfree.tv/genre/' + genre + '/page/' + str(page)
    vost = Page()
    soup = vost.getSoup(url)
    anime['url'] = url
    anime['page'] = page
    anime['animes'] = vost.getAnimes(soup)
    return anime