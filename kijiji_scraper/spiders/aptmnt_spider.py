import scrapy
from .. import items

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class KijijiAptmntSpider(CrawlSpider):
    name = "kijiji_aptmnt_spider"
    allowed_domains = ["kijiji.ca"]
    start_urls = ["http://www.kijiji.ca/b-apartments-condos/ottawa/c37l1700185"]     
    rules = [
        Rule(
            LinkExtractor(
                allow=["http://www.kijiji.ca/v-\d-bedroom-apartments-condos/ottawa/.+"]
            ), 
            callback='parse_item'),
    ]

    def parse_item(self, response):
        aptmnt = items.AptmntItem()

        aptmnt["url"] = response.url
        aptmnt["address"] = self._extract_field(response, "Address")
        aptmnt["price"] = self._extract_field(response, "Price")
        aptmnt["date_listed"] = self._extract_field(response, "Date Listed")
        
        return aptmnt

    def _extract_field(self, response, fieldname):
        l = response.xpath("//th[text()='{0}']/following::td[1]//./text()".format(fieldname)).extract()
        return l[0] if l else None

