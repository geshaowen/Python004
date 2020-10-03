# 作业一：
# 安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。

# 导入 requests、bs4 库
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from time import sleep

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)

# print(response.text)

bs_info = bs(response.text, 'html.parser')

# 用 for 循环,获取前 10 个电影名称、电影类型和上映时间
movie_details = []
urls = set()
for tags in bs_info.find_all('div', attrs={'class': 'movies-list'}):
    for atag in tags.find_all('a', limit=30):
        # print(atag)
        # 获取所有链接,并添加到列表中
        link ='https://maoyan.com' + atag.get('href')
        print(link)
        urls.add(link)
        # print(urls)
        # 防止爬虫被禁
        sleep(1)
    print(urls)

# 电影详情页面获取名称、类型、上映时间等信息
def movie_info(url):
    response = requests.get(url, headers=header)

    bs_info = bs(response.text,'html.parser')

    tags = bs_info.find('div',attrs={'class':'movie-brief-container'})
    # print(tags)

    movie_name = tags.find('h1',attrs={'class': 'name'}).string # 获取电影名称

    movie_type = []

    subtags = tags.find_all('li', attrs={'class':'ellipsis'})
    # print(subtags)

    movie_type_tags = subtags[0].find_all('a')
    for tag in movie_type_tags:
        movie_type.append(tag.string)

    movie_date = subtags[-1].string  # 获取电影上映日期

    movie_details.append([movie_name, movie_type, movie_date])

# 获取电影信息
for url in urls:
    movie_info(url)
    

# 写入文件
movies = pd.DataFrame(data = movie_details)

movies.to_csv('./作业一.csv', encoding='utf8', index=False, header=False)
        




