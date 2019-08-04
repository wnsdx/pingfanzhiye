# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PingfanzhiyeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    chapter_name = scrapy.Field()
    link_url = scrapy.Field()
    img_urls = scrapy.Field()
    img_url = scrapy.Field()
    img_name = scrapy.Field()
    image_paths = scrapy.Field()
    pass
