# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class DapentiItem(Item):
    title = Field()
    time = Field()
    participator  = Field()
    # bottomline = Field()
    # duty = Field()
    # xxx = Field()
