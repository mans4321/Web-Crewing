# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebScrapingItem(scrapy.Item):
    # The name field will represent the url of the page
    # The content field will represent the extracted text content of that page
    name = scrapy.Field()
    content = scrapy.Field()
    pass
