import time		
import  scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from tutorial.items import urlMap
from scrapy.selector import Selector
from w3lib.html import remove_tags


class MySpider(CrawlSpider):
    name = "ikea.com"
    #allowed_domains = ['ikea.com']
    start_urls = ['http://www.ikea.com']
	#scrape_target = "building"

    rules = [(Rule(SgmlLinkExtractor(), callback='parse_url', follow=False, process_links=None)),
	#Rule(Rule(SgmlLinkExtractor(), callback='end_parse', follow=False))

	]

    def parse_url(self, response):
		xSrchString = '//*[contains(text(),"explore")]'
		item = urlMap()
		
		closeable = 0
		#item['category'] = "searching"
		#if(closeable == 1):
		#	raise scrapy.exceptions.CloseSpider(reason='Target_Found')
		#closeable = 0
		#item['url'] = response.url
		#item['url'] = response.xpath('//title/text()').extract()
		#successfully extracts titles: item['urlDict'] = {'searching' : response.xpath('//title/text()').extract()}
		#item['urlDict'] = {'searching' : response.xpath('//*/text()[normalize-space(.)="explore"]/parent::*').extract()} 		
		
		#item['urlDict'] = {'searching' : response.xpath('//*[matches(text(),"(^|\W)explore($|\W)","i")]').extract()}	only xpath 2.0
		
#		def spider_closed(self, spider):
#			item['urlDict'] = {'foundTarget' : response.url}
#			item['targetNode'] = {remove_tags(response.xpath('//*[contains(text(),"explore")]').extract_first())}
#			print "spider closed!"
#			return item;


#		if (response.xpath(xSrchString)):
#			yield bigItem( 
#			item['urlDict'] = {'foundTarget' : response.url}
#			item['targetNode'] = {remove_tags(response.xpath('//*[contains(text(),"explore")]').extract_first())}
#			callback=self.end_parse
#			)
			#raise scrapy.exceptions.CloseSpider(reason='Target_Found')
			#closeable == 1
			#return item;
				
		if (response.xpath(xSrchString)):
			#yield end_parse(response)
			item['urlDict'] = {'foundTarget' : response.url}
			item['targetNode'] = {remove_tags(response.xpath('//*[contains(text(),"explore")]').extract_first())}
			
			#callback=self.end_parse
			#)
			#raise scrapy.exceptions.CloseSpider(reason='Target_Found')
			closeable == 1
			print "i'm in parse url\n"
			#return item;
		else:
			item['urlDict'] = {'searching' : response.url}
			#yield item;

		return item 

	

    def end_parse(self, response):
		#item['urlDict'] = {'foundTarget' : response.url}
		#item['targetNode'] = {remove_tags(response.xpath('//*[contains(text(),"explore")]').extract_first())}
		#raise scrapy.exceptions.CloseSpider(reason='Target_Found')
		#if(response.xpath(xSrchString)):
		print "i'm in end_parse\n"
		if (response.xpath(xSrchString)):
			#yield end_parse(response)
			item['urlDict'] = {'foundTarget' : response.url}
			return item
		#if(closeable == 1):
		#	raise scrapy.exceptions.CloseSpider(reason='Target_Found')

		#item['urlDict'] = {'searching' : response.xpath('//*[contains(text(),"explore")]').extract()}	#works

		#links = "More Ikea websites to explore"

		#for link in response.xpath(("a::text").re.match(r'(.*) explore (.*?) .*', line, re.I).extract()
			#testword = link.xpath("a::text").re.match(r'(.*) explore (.*?) .*', line, re.I)
			#testword = link
			#print link
			#break

		#for link in response.xpath('//a[text()="explore"]/@href').extract():
		#	yield item(category="found")
		#	yield item(url=link)
		#	i = i+1
		#	if i==25:
		#		scrapy.exceptions.CloseSpider(reason='cancelled')
		#if('//a[text()=="1999"]').extract():
		#	item['category'] = "found"
		#	item['url'] = response.url
		#if i==25:
		#	scrapy.exceptions.CloseSpider(reason='cancelled')
		
		
		#url_map = {}
		#url_map['url'] = response.url
		
		#return url_map

