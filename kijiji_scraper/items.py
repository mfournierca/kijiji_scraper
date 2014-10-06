# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AptmntItem(scrapy.Item):
    url = scrapy.Field()
    address = scrapy.Field()
    price = scrapy.Field()
    date_listed = scrapy.Field() 
    num_bedrooms = scrapy.Field()
    num_bathrooms = scrapy.Field() 
    description = scrapy.Field()
    title = scrapy.Field()

