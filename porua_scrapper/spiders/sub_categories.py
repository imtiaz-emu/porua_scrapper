import scrapy, json, pdb, os.path
from porua_scrapper.items import SubCategory
from porua_scrapper.config import SITE_URL
from scrapy.selector import HtmlXPathSelector


class SubCategoriesSpider(scrapy.Spider):
    name = "sub_categories"
    start_urls = []

    file_path = 'data/categories.json'

    #if os.path.exists(file_path):

    with open(file_path, encoding='utf-8') as data_file:
        try:
            categories = json.loads(data_file.read())

            for data in categories:
                start_urls.append(data['url'])
        except:
            pass
    def parse(self, response):
        #hxs = HtmlXPathSelector(response)

        #category_name = hxs.select("//section[@id='bookCategory']//div[@class='leftMenuArea pull-left']//ul[@class='catTree']//li/text()").extract_first()

        category_name = response.css('ul.catTree li::text').extract_first()

        for sub_category in response.css('ul.catTree li ul li'):
            sub_category_obj = SubCategory()

            sub_category_obj['name'] = sub_category.css('a::text').extract_first()
            sub_category_obj['url'] = SITE_URL + sub_category.css('a::attr(href)').extract_first()
            sub_category_obj['category_name'] = category_name

            yield sub_category_obj


