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
        movies = Selector(response=response).xpath('//div[@class="movies-list"]')
        for i in range(10):
            # title = movies[i].xpath('./span[1]/text()')
            # tags = movies[i].xpath('./span[3]/text()')
            # play_time = movies[i].xpath('./span[4]/text()')
            
            link = 'https://maoyan.com' + movies[i].xpath('./a/@href').extract_first()
            yield scrapy.Request(url=link, callback=self.parse2)
    

    def parse2(self, response):
        movie_info = Selector(response=response).xpath('//div[@class="movie-brief-container"]')

        item = MaoyanItem()

        # 电影名称
        title = movie_info.xpath('./h1/text()')

        # 电影类型
        tags = movie_info.xpath('./ul/li[1]/a/text()')

        # 上映日期
        play_time = movie_info.xpath('./ul/li[3]/text()')

        item['title'] = title
        item['tags'] = tags
        item['play_time'] = play_time

        yield item
