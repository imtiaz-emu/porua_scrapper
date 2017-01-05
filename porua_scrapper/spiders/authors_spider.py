import scrapy
from porua_scrapper.items import Author
from porua_scrapper.config import SITE_URL


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    start_urls = []
    for I in range(1,847):
        url = SITE_URL + "/book/authors?page=" + str(I)
        start_urls.append(url)

    def parse(self, response):

        for author in response.css('ul.authorList li'):
            file_path = open('author_urls.txt', 'a')
            file_path.write(SITE_URL + author.css('a::attr(href)').extract_first() + '\n')
            file_path.close()
