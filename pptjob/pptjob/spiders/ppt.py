# -*- coding: utf-8 -*-
import scrapy


class PptSpider(scrapy.Spider):
    name = 'ppt'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['http://www.ptt.cc/']

    def parse(self, response):
        pass
