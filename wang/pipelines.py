# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import re

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

images_store = "images"


class MyPipeline(object):
    def process_item(self, item, spider):
        return item


class WangPipeline(ImagesPipeline):

    # def get_media_requests(self, item, info):
    #     #把图片链接发给调度器
    #     yield scrapy.Request(url = item['image_urls'])

    # def get_media_requests(self, item, info):
    #     image_link = item['image_urls']
    #     yield scrapy.Request(url = image_link)
    #
    # def item_completed(self, results, item, info):
    #     print(item)
    #     image_path = [x['path'] for ok, x in results if ok]
    #     print('图片路径是：', images_store + image_path[0])
    #     os.rename(images_store + '/' + image_path[0], images_store + '/' + item["image_name"] + '.jpg')
    #     return item
    def get_media_requests(self, item, info):
        image_url = item['image_urls']
        yield scrapy.Request(image_url, meta={'name': item['image_name']})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

    def file_path(self, request, response=None, info=None):
        name = request.meta['name']  # 接收上面meta传递过来的图片名称
        name = re.sub(r'[？\\*|“<>:/]', '', name)  # 过滤windows字符串，不经过这么一个步骤，你会发现有乱码或无法下载
        filename = name + '.jpg'  # 添加图片后缀名
        return filename