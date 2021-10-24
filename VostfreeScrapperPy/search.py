from VostfreeScrapperPy.vostfree import SearchPage

def getSearchTerm(SearchTerm):
    anime= {}
    SearchTerm = SearchTerm.replace(" ", "+")
    url =  'https://vostfree.tv/index.php?do=search&subaction=search&search_start=0&full_search=0&result_from=1&story=' + SearchTerm
    vost = SearchPage()
    soup = vost.getSoup(url)
    anime['url'] = url
    anime['animes'] = vost.getAnimes(soup)
    return anime