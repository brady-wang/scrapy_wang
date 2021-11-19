import scrapy

from wang.items import WangItem
from wang.pipelines import WangPipeline
class NewsSpider(scrapy.Spider):
    name = 'photo'
    allowed_domains = ['meishij.net']
    start_urls = ['https://www.meishij.net/china-food/caixi/qingzhencai/']
    page = 1

    def parse(self, response):
        item = WangItem()
        image_urls = response.xpath('//*[@id="listtyle1_list"]/div/a/img/@src').extract()
        image_name = response.xpath('//*[@id="listtyle1_list"]/div/a/div/div/div[1]/strong/text()').extract()
        for i in range(0, len(image_name)):
            item['image_urls'] = image_urls[i]
            item['image_name'] = image_name[i]
            yield item
            self.page += 1
        # if self.page < 5:  # 只爬前5页
        #     url = "https://www.meishij.net/china-food/caixi/qingzhencai/?&page=" + str(self.page)
        #     yield scrapy.Request(url, callback=self.parse)