# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Quote(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()

class Category(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()

class SubCategory(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    categoryName = scrapy.Field()

class Author(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    photo = scrapy.Field()
    biodata = scrapy.Field()



