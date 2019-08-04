# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from lxml import etree
from ..items import PingfanzhiyeItem


class PingfanzhiyeSpider(scrapy.Spider):
    name = 'PingFanZhiYe'
    allowed_domains = ['https://www.mkzhan.com/214130/']
    start_urls = ['https://www.mkzhan.com/214130/']
    # chapterurl = ['https://www.mkzhan.com/214130/%s']

    def parse(self, response):

        pass

        # 从start_requests发送请求
    def start_requests(self):
        print('[start_url]=',self.start_urls[0])
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse1)

    # 解析response,获得章节图片链接地址
    def parse1(self,response):
        items = []
        chapters = []
        # html = response.body.decode()
        # print('[html]=',html,r'[/html]')

        # chapters = response.xpath('//ul[class="chapter__list-box clearfix hide"]/li/a')#.extract()
        chapters = response.xpath('//ul[@class="chapter__list-box clearfix hide"]/li')#.extract()
        # print('[chapters]=',chapters)
        for chapter in chapters:
            item = PingfanzhiyeItem()
            # print('[chapter]=',chapter)

            # 章节链接地址
            url = chapter.xpath('./a/@data-chapterid').extract()
            # print('[chapter url]=', url)
            item['link_url'] = self.start_urls[0] + url[0]

            # 章节名
            chapter_name = chapter.xpath('./a[@class="j-chapter-link"]/text()').extract()[0].strip()
            # print('[chapter_name]=', chapter_name)
            item['chapter_name'] =chapter_name

            items.append(item)

        for item in items:
            # print("[item['link_url']]=",item['link_url'])
            # print("[item['chapter_name']]=", item['chapter_name'])
            yield scrapy.Request(url=item['link_url'],meta={'item':item},dont_filter=True,callback=self.parse2)

    def parse2(self,response):
        items = []
        html = response.body.decode()
        # print('[parse2]response=',html)
        item_parse1 = response.meta['item']
        print('[parse2]item',item_parse1)

        imgs = response.xpath('//img[@class="lazy-read"]')#.extract()
        for img in imgs:
            pass
            item = PingfanzhiyeItem()
            # print('[parse2]img=',img)
            item['chapter_name'] = item_parse1['chapter_name']
            print('[chapter_name]=', item['chapter_name'])
            img_url = img.xpath('@data-src').extract()
            print('[img_url]=',img_url[0])
            item['img_url']=img_url[0]
            img_name = img.xpath('@alt').extract()
            print('[img_name]=', img_name[0])
            item['img_name'] = img_name[0]
            items.append(item)

        for item in items:
            print("item['img_url']=",item['img_url'])
            print('item[img_name]=', item['img_name'])
            yield item

        # for item in items:
        #     yield scrapy.Request(url=item['img_url'], meta={'item': item}, callback=self.parse)
        pass