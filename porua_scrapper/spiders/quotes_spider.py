import scrapy
from porua_scrapper.items import Category, SubCategory, Author, Quote
from porua_scrapper.config import SITE_URL2


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = []
    for I in range(2):
        url = SITE_URL2 + "page/" + str(I+1)
        start_urls.append(url)

    # print(start_urls)


    def parse(self, response):
        for quote in response.css('div.quote'):
            quoteObj = Quote()

            quoteObj['text'] = quote.css('span.text::text').extract_first()
            quoteObj['author'] = quote.css('span small::text').extract_first()
            quoteObj['tags'] = quote.css('div.tags a.tag::text').extract()

            yield quoteObj

