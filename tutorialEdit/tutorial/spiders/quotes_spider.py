#import scrapy


# class QuotesSpider(scrapy.Spider):
    # name = "quotes"

    # def start_requests(self):
        # urls = [
            # 'http://quotes.toscrape.com/page/1/',
            # 'http://quotes.toscrape.com/page/2/',
        # ]
        # for url in urls:
            # yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
            # f.write(response.body)
        # self.log('Saved file %s' % filename)
		
import  scrapy

from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field


class MySpider(CrawlSpider):
    name = "ikea.com"
    allowed_domains = ['ikea.com']
    start_urls = ['http://www.ikea.com']

    rules = (Rule(SgmlLinkExtractor(), callback='parse_url', follow=False), )

    def parse_url(self, response):
		#item = MyItem()
		#item['url'] = response.url
		#return item
		item = {}
		item['url'] = response.url
		return item