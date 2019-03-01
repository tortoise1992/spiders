# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AhuiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    card_name_zn=scrapy.Field()
    card_name_ja = scrapy.Field()
    card_name_en = scrapy.Field()
    card_keys=scrapy.Field()
    card_origin = scrapy.Field()
    card_level = scrapy.Field()
    card_type = scrapy.Field()
    card_code = scrapy.Field()
    card_ak = scrapy.Field()
    card_dk = scrapy.Field()
    pass
