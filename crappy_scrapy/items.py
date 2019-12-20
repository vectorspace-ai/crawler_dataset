# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

class ScrapyItem(scrapy.Item):

    name=scrapy.Field(
    	input_processor=MapCompose(remove_tags),
    	output_processor=TakeFirst()
    	)
    about_text = scrapy.Field(
    	input_processor=MapCompose(remove_tags),
    	output_processor=TakeFirst()
    	)
