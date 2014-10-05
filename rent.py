#!/usr/bin/env python2.7

from scrapy import Item, Field
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class AptmntItem(Item):
    url = Field()
    address = Field()
    #price = Field()
    #date_listed = Field()

class KijijiOneBedAptmntOttawaSpider(CrawlSpider):
    
    name = "kijiji_onebed_ottawa"
    allowed_domains = ["kijiji.ca"]
    start_urls = ["http://www.kijiji.ca/b-apartments-condos/ottawa/c37l1700185"]
    rules = [Rule(LinkExtractor(allow=["http://www.kijiji.ca/v-1-bedroom-apartments-condos/ottawa/.+"]), 'parse_aptmnt')]

    def parse_aptmnt(self, response):
        aptmnt = AptmntItem()
        aptmnt["url"] = response.url
        aptmnt["address"] = response.xpath("//th[text()='Address']/following::td/text()").extract()
