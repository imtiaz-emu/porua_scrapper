import scrapy
from porua_scrapper.items import Author
from porua_scrapper.config import SITE_URL
from scrapy.selector import HtmlXPathSelector
import pdb


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    site_link = SITE_URL + '/book/authors'
    start_urls = [site_link]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        authors = hxs.select("//section[@id='authorList']/div[@class='container']/ul//li")

        for author in authors:
            author_obj = Author()
            author_obj['name'] = author.select("a/h2/text()").extract_first()
            author_obj['url'] = SITE_URL + author.select("a/@href").extract_first()
            yield author_obj

            # file_path = open('author_urls.csv', 'a')
            # file_path.write(SITE_URL + link + '\n')
            # file_path.close()

        next_page = response.xpath("//div[@class='pagination']//a[position() = (last())]/@href").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
