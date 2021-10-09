# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Crawler1Item(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    about = scrapy.Field()
    pass