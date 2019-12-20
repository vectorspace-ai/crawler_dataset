import scrapy

from crappy_scrapy.utils import get_symbols
from crappy_scrapy.items import ScrapyItem
from scrapy.loader import ItemLoader

URL='https://www.reuters.com/companies/'

market='.O'

class reuters_spider(scrapy.Spider):
	name='Reuters Spider'
	handle_httpstatus_list = [404, 500]


	def start_requests(self):
		symbols=get_symbols(market)
		for symbol in symbols:
			yield scrapy.Request(url=f"{URL}{symbol}", callback=self.parse, meta={'symbol': symbol})
	def parse(self, response):
		for name in response.xpath('//*[@id="__next"]/div/div[3]'):
			l=ItemLoader(item=ScrapyItem(), selector=name)
			l.add_xpath('name', '//*[@id="__next"]/div/div[3]/div/div/div[1]/div[1]/div[1]/p')
			yield l.load_item()

		for about in response.xpath('//*[@id="__next"]/div/div[4]/div[1]/div/div/div/div[4]/div[1]'):	
			l=ItemLoader(item=ScrapyItem(), selector=about)
			l.add_xpath('about_text', '//*[@id="__next"]/div/div[4]/div[1]/div/div/div/div[4]/div[1]/p')
			yield l.load_item()