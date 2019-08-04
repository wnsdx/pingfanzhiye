# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pingfanzhiye import settings
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

import os
import sys

class PingfanzhiyePipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     # print('[PingfanzhiyePipeline]item=\n',item)
    #     # yield Request(item['img_url'],meta={'name':item['img_name']})
    #     return item

    def get_media_requests(self,item,info):
        print('[%s]item='%(sys._getframe().f_code.co_name),item)

        yield Request(item['img_url'], meta={'name': item['img_name'],'chapter_name': item['chapter_name']})

        # for image_url in item:
            # print('[pipelines get_media_requests]image_url=',image_url)
            # yield Request(item['img_url'], meta={'name': item['img_name']})
        pass

    def file_path(self,request,response=None,info=None):
        print('[%s]request.url='%(sys._getframe().f_code.co_name),request.url)
        print("[%s]request.meta['name']="%(sys._getframe().f_code.co_name),request.meta['name'])
        print("[%s]request.meta['chapter_name']=" % (sys._getframe().f_code.co_name), request.meta['chapter_name'])
        filename= u'{0}/{1}'.format(request.meta['chapter_name'],request.meta['name'])
        return filename
        pass