# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem
import os
import datetime
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['https://bbs.hupu.com']
    start_urls = ('https://bbs.hupu.com/selfie-type3',)
    domain = 'https://bbs.hupu.com'
    base_dir = '/Users/JohnsonJohnson/PycharmProjects/mySpider/mySpider/spiders'
    img_urls = []

    rules = (
        Rule(LinkExtractor(allow='.*selfie-type3.*'),callback='parse',follow=True),
        # Rule(LinkExtractor(allow='https://bbs.hupu.com/\d+.html', deny=''),callback='parse_item', follow=True),
    )

    def parse(self, response):

        # filename = "teacher.html"
        # open(filename, 'wb').write(response.body)
        items = []
        tmp = response.xpath("//form[@id='ajaxtable']/div[@class='show-list']/ul[@class='for-list']/*")
        #
        for each in tmp:
            # 将我们得到的数据封装到一个 `ItcastItem` 对象
            item = MyspiderItem()
            # extract()方法返回的都是unicode字符串
            url = each.xpath("div[@class='titlelink box']/a[@class='truetit']/@href").extract_first()
            name = each.xpath("div[@class='titlelink box']/a[@class='truetit']/text()").extract()

            # xpath返回的是包含一个元素的列表
            item['url'] =  self.domain + url
            item['name'] = name

            # yield item

            items.append(item)

        # 直接返回最后数据
        return items
    def parse_item(self,response):
        pass
        # print(response.url)
