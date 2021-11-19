# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import re

import scrapy
from scrapy.pipelines.images import ImagesPipeline


images_store = "images"


class MyPipeline(object):
    def process_item(self, item, spider):
        return item


class WangPipeline(ImagesPipeline):

    def process_item(self, item, spider):
        print(3333333333)
        return item

    def get_media_requests(self, item, info):
        image_urls = item['image_urls']

        yield scrapy.Request(image_urls)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        print('图片路径是：', images_store + image_path[0])
        os.rename(images_store + '/' + image_path[0], images_store + '/' + item["image_name"] + '.jpg')
        return item
