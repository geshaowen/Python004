# 作业一：
# 安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。

# 导入 requests、bs4 库
import requests
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)

bs_info = bs(response.text, 'html.parser')

# 用 for 循环,获取前 10 个电影名称、电影类型和上映时间
for tags in bs_info.find_all('div', attrs={'class': 'movie-item-hover'}):
    for atag in tags.find_all('a'):
        print(atag.get('href'))
        # 获取所有链接
        print(atag.find('span').text)
        # 获取电影名字


