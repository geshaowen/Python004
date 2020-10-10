# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from maoyan.items import MaoyanItem

class MaoyanmoviesSpider(scrapy.Spider):
    name = 'maoyanmovies'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')

        item = MaoyanItem()

        for i in range(10):
             title = movies[i].xpath('./div[1]/@title').extract_first()
             tags = movies[i].xpath('./div[2]/text()').extract()[1].strip()
             play_time = movies[i].xpath('./div[4]/text()').extract()[1].strip()

             item['title'] = title
             item['tags'] = tags
             item['play_time'] = play_time

             yield item
    

