from page import getLastNewsPage, getAnimesByGenreAndPage
from search import getSearchTerm
from anime import getAnimeById, getAnimeByUrl

print(getAnimeById(618))
print('\n')
print(getAnimeByUrl('https://vostfree.tv/1062-selection-project-vostfr-ddl-streaming-1fichier-uptobox.html'))
print('\n')
print(getSearchTerm('Kaguya-Sama Wa Kokurasetai - Tensai-Tachi No Renai Zunousen'))
print('\n')
print(getLastNewsPage(1));
print('\n')
print(getAnimesByGenreAndPage('Action', 2))