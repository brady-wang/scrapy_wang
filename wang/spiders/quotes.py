import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        if response.status == 200:
            print("crawl url " + response.url)
            lis = response.xpath('//div[@class="quote"]')
            item = {}
            if len(lis) > 0:
                for li in lis:
                    author = li.xpath(".//small[@class='author']/text()").extract_first()
                    item['author'] = author
                    yield item

                # nextPage = response.xpath('//ul[@class="pager"]//li[@class="next"]//a/@href').extract_first();
                # print(nextPage)
                # if nextPage is not None:
                #     url = response.urljoin(nextPage)
                #     yield scrapy.Request(url, self.parse)