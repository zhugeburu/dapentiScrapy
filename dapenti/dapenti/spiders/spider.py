#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from dapenti.items import DapentiItem
from scrapy import Request

class DPTSpider(scrapy.Spider):
	name = "dapenti"
	allowed_domains = ["dapenti.com"]
	start_urls = ["http://www.dapenti.com/blog/index.asp"]
	def parse(self,response):
		req = []
		sels = response.xpath('//*[@id="center"]/table[1]/tbody/tr[2]/td[1]/div/ul/li')
		reqs = []
		for sel in sels:
			url = "http://dapenti.com/blog/" + sel.css('a::attr(href)').extract_first()
			print "dep1 " + url
			req = Request(url,callback=self.parse_item)
			reqs.append(req)
		return reqs

	def parse_item(self,response):
		item = DapentiItem()
		if(response.status != 200 ):print "Fail to request : ",response.url
		print "dep2 " + response.url
		item['title'] = response.xpath('/html/body/table/tbody/tr/td[1]/div/table[1]/tbody/tr[1]/td/div/span/span/a[2]/text()').extract_first()
		item['time'] = response.css('body > table > tbody > tr > td.oblog_t_2 > div > table.ke-zeroborder > tbody > tr:nth-child(2) > td > table:nth-child(1) > tbody > tr > td > div > span::text').extract()[0][-18:]
		item['participator'] = response.xpath('//*[@id="SOHU_MAIN"]/div[1]/div[1]/div[1]/div/a/span/span/em/text()').extract_first()
		try:
			print repr(item).decode("unicode-escape") + '\n'
		except UnicodeEncodeError:
			print u'解码发生错误'
		return item
