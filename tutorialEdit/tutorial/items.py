# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# class TutorialItem(scrapy.Item):
#    define the fields for your item here like:
#    name = scrapy.Field()
    # pass

# class IkeaItem(Item):
    # name = scrapy.Field()
    # link = scrapy.Field()
	
class urlMap(scrapy.Item):
	searching = scrapy.Field()
	foundTarget = scrapy.Field()
	reachedMax = scrapy.Field()
	url = scrapy.Field()
	maxURLs = scrapy.Field()
	scrapeTarget = scrapy.Field()
	urlDict = scrapy.Field()
	targetNode = scrapy.Field()
	foundGen = scrapy.Field()

	
