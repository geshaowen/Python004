# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd

class MaoyanPipeline:
    def process_item(self, item, spider):
        title = item['title']
        tags = item['tags']
        play_time = item['play_time']

        movie_detail = [title, tags, play_time]

        movie_file = pd.Dataframe(data = movie_detail)

        movie_file.to_csv('./maoyan.csv', mode='a', encoding = 'utf-8', index=False, header=False)

        return item
