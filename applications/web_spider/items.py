# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PageContentItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    raw_content = scrapy.Field()
    content = scrapy.Field()
    meta_title = scrapy.Field()
    meta_description = scrapy.Field()
    meta_keywords = scrapy.Field()
    canonical = scrapy.Field()
