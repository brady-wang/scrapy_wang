import scrapy


class Taobao3Spider(scrapy.Spider):
    name = 'taobao3'
    allowed_domains = ['taobao.com']
    start_urls = ['http://taobao.com/']

    def parse(self, response):
        pass
