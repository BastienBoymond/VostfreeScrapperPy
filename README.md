<div align="center">
    <h1>VostfreeScrapperPy</h1>

[![Pypi](https://img.shields.io/pypi/dm/VostfreeScrapperPy?label=Download&color=brightgreen&logo=python&style=for-the-badge)](https://pypi.org/project/VostfreeScrapperPy/)
[![Pypi](https://img.shields.io/pypi/v/VostfreeScrapperPy?label=Version&color=brightgreen&logo=python&style=for-the-badge)](https://pypi.org/project/VostfreeScrapperPy/)
    <br>
    <strong>Python Scrapper of <a href="https://vostfree.tv/">vostfree.tv</a> website</strong>
    <br>
    <small><strong><a href="https://github.com/BastienBoymond/VostfreeScrapperJs">This Scrapper exist in Js</a></strong></small>
</div>

## 📓 Description 📓

This Scrapper is a Python Scrapper of vostfree.tv website.
He get a lot of information like:

* Main Page
* Anime Page
* Search Page
* Genre Page

## 📦 Installer 📦

* Clone the repository

        git@github.com:BastienBoymond/VostfreeScrapperPy.git

* Install the requirements

        pip install BeautifulSoup4
        pip install requests

* Use it

    You get this function:

        getAnimeById(id)
        getAnimeByUrl(url)
        getLastNewsPage(page)
        getAnimesByGenreAndPage(genre, page)
        getSearchTerm(SearchTerm)

If your lost you get the test.py to see exemple of use.
