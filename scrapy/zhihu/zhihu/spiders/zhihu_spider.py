# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request,FormRequest

# import scrapy
from zhihu.items import ZhihuItem
from zhihu.settings import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    allowed_domains = ["zhihu.com"]
    start_urls = [
        "https://www.zhihu.com/#signin"
    ]

    rules = (
        Rule(LinkExtractor(allow=('/question/\d+#answer-\d+')), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=('/question/\d+')), callback='parse_item', follow=True)
    )

    def __init__(self):
        self.headers=HEADER
        self.cookies=COOKIES

    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            yield FormRequest(
                url, meta = {'cookiejar': i},
                headers=self.headers,
                cookies=self.cookies,
                callback=self.parse_item)

    def parse_item(self, response):
        # print response.body
        selector = Selector(response)

        # print 'Start extract data from response ..............'
        items = []
        for elem in selector.xpath('//div[@class="feed-content"]/h2[@class="feed-title"]'):
            item = ZhihuItem()
            item['title'] = elem.xpath('a/text()').extract()
            item['link']  = elem.xpath('a/@href').extract()
            items.append(item)

            print(item['title'].decode())
            print(item['link'].decode())
        # print 'Finish extract data........................'
        return items
