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
			print url
			req = Request(url,callback = self.parse_1)
			reqs.append(req)
		return reqs

	def parse_1(self,response):
		item = DapentiItem()
		print response.url
		item['title'] = response.xpath('/html/body/table/tbody/tr/td[1]/div/table[1]/tbody/tr[1]/td/div/span/span/a[2]/text()').extract_first()
		item['time'] = response.css('body > table > tbody > tr > td.oblog_t_2 > div > table.ke-zeroborder > tbody > tr:nth-child(2) > td > table:nth-child(1) > tbody > tr > td > div > span::text').extract()[0][-18:]
		item['participator'] = response.xpath('//*[@id="SOHU_MAIN"]/div[1]/div[1]/div[1]/div/a/span/span/em/text()').extract_first()
		print repr(item).decode("unicode-escape") + '\n'
		return item
