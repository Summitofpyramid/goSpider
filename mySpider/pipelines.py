# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class MyspiderPipeline(ImagesPipeline):
    def process_item(self, item, spider):
        return item
    # def get_media_requests(self, item, info):
    #     for image_url in item['image_urls']:
    #         yield scrapy.Request(image_url)
    #
    # def item_completed(self, results, item, info):
    #     image_paths = [x['path'] for ok, x in results if ok]
    #     if not image_paths:
    #         raise DropItem('Item contains no images!')
    #     return item
