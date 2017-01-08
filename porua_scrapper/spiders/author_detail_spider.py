import scrapy, json, pdb
from porua_scrapper.items import Author
from porua_scrapper.config import SITE_URL
from scrapy.selector import HtmlXPathSelector


class AuthorDetailsSpider(scrapy.Spider):
    name = "author_details"
    site_link = SITE_URL + '/book/authors'
    start_urls = []

    with open('data/authors.json', encoding='utf-8') as data_file:
        authors = json.loads(data_file.read())

        for data in authors:
            start_urls.append(data['url'])

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        author_obj = Author()
        author_obj['name'] = hxs.select("//section[@id='bookAuthor']//div[@class='container-fluid authorHeader']//div[@class='authDes']//h1/text()").extract_first()
        author_obj['url'] = response.meta['redirect_urls'][0]
        author_obj['short_description'] = hxs.select("//section[@id='bookAuthor']//div[@class='container-fluid authorHeader']//div[@class='authDes']//p[@class='des']/text()").extract_first()
        author_obj['image_urls'] = SITE_URL + hxs.select("//section[@id='bookAuthor']//img[@class='authImg']/@src").extract_first()

        yield author_obj
