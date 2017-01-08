import scrapy, pdb
from porua_scrapper.items import Author
from porua_scrapper.config import SITE_URL
from scrapy.selector import HtmlXPathSelector


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    site_link = SITE_URL + '/book/authors'
    start_urls = [site_link]

    def parse(self, response):

        ''' Grab all author list and browse pagination '''

        hxs = HtmlXPathSelector(response)

        authors = hxs.select("//section[@id='authorList']/div[@class='container']/ul//li")

        for author in authors:
            author_obj = Author()
            author_obj['name'] = author.select("a/h2/text()").extract_first()
            author_obj['url'] = SITE_URL + author.select("a/@href").extract_first()
            yield author_obj

        next_page = response.xpath("//div[@class='pagination']//a[position() = (last())]/@href").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
