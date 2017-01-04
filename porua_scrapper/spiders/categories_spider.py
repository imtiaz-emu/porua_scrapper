import scrapy
from porua_scrapper.items import Category
from porua_scrapper.config import SITE_URL
import json


class CategoriesSpider(scrapy.Spider):
    name = "categories"
    start_urls = []
    for I in range(2):
        url = SITE_URL + "book/categories?page=" + str(I+1)
        start_urls.append(url)

    print(start_urls)


    def parse(self, response):
        # print(response.css('ul.categoryList li div.pFIrstCatCaroItem a').extract_first())

        for category in response.css('ul.categoryList li'):
            categoryObj = Category()

            categoryObj['name'] = category.css('div.bookSubjectCaption h2::text').extract_first()
            categoryObj['url'] = category.css('a::attr(href)').extract_first()

            yield json.loads(categoryObj)

