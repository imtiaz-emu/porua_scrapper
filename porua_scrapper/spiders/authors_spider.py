import scrapy
from porua_scrapper.items import Author
from porua_scrapper.config import SITE_URL
from scrapy.selector import HtmlXPathSelector
import pdb

class AuthorsSpider(scrapy.Spider):
    name = "authors"
    site_link = SITE_URL + '/book/authors'
    start_urls = [site_link]

    # for I in range(1,847):
    #     url = SITE_URL + "/book/authors?page=" + str(I)
    #     start_urls.append(url)

    def parse(self, response):
        self.author_link_list = []
        self.parse_author_urls(response)
        pdb.set_trace()
        #pdb.set_trace()
        # for author in response.css('ul.authorList li'):
        #     file_path = open('author_urls.txt', 'a')
        #     file_path.write(SITE_URL + author.css('a::attr(href)').extract_first() + '\n')
        #     file_path.close()

    def parse_author_urls(self, response):
        hxs = HtmlXPathSelector(response)

        authors = hxs.select("//section[@id='authorList']/div[@class='container']/ul//li")

        #author_link_list = []
        for author in authors:
            name = author.select("a/h2/text()").extract_first()
            link = author.select("a/@href").extract_first()
            # file_path = open('author_urls.txt', 'a')
            # file_path.write(SITE_URL + link + '\n')
            # file_path.close()
            self.author_link_list.append({'name': name, 'link': SITE_URL + link})

        next_page = response.xpath("//div[@class='pagination']//a[position() = (last())]/@href").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_author_urls)