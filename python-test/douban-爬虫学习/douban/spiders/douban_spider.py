# -*- coding: utf-8 -*-
import scrapy

from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫名 不能和项目名重复
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口url，扔到调度器里去
    start_urls = ['http://movie.douban.com/top250']
    # 默认解析方法
    def parse(self, response):
        # 循环电影的列表
        move_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i in move_list:
            douban_item = DoubanItem()
            # 写详细的 xpath， 进行规则解析数据 
            # extract_first()  获取第一个数据
            # extract() 获取所有数据
            douban_item['number'] = i.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['name'] = i.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            douban_item['star'] = i.xpath(".//div[@class='info']/div[@class='bd']//span[@class='rating_num']/text()").extract_first()
            douban_item['evaluate'] = i.xpath(".//div[@class='info']//div[@class='star']/span[4]/text()").extract_first()
            douban_item['describe'] = i.xpath(".//div[@class='info']/div[@class='bd']//span[@class='inq']/text()").extract_first()
            content = i.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            # 数据处理
            for x in content:
                content_s = "".join(x.split())
                douban_item['introduce'] = content_s
            # 你需要把数据 yield 到 pipelines 里面去
            yield douban_item
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        # 解析下一页
        if next_link:
            next_link = next_link[0]
            # 满足下一页条件，则 传入 路径，并且调用回调函数， self.parse 去解析爬到的内容
            yield scrapy.Request("http://movie.douban.com/top250" + next_link, callback=self.parse)