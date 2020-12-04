import time
import requests
from lxml import etree
from time import sleep
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers = {
    'User-Agent': ua.random,
    'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony'
}

s = requests.Session()
login_url = 'https://accounts.douban.com/j/mobile/login/basic'
form_data = {
    'ck': '',
    'remember': 'true',
    'name': 'wuqw5666@163.com',
    'password': 'hanyan839100'
}

pre_login = 'https://accounts.douban.com/passport/login'
pre_resp = s.get(pre_login, headers = headers)

response = s.post(login_url, data=form_data, headers = headers, cookies = s.cookies)

def get_movies_list(top250url):
    response2 = requests.get(top250url, headers=headers)
    selector = etree.HTML(response2.text)

    film_name = selector.xpath('//div[@class="hd"]/a/span[1]/text()')
    film_link = selector.xpath('//div[@class="hd"]/a/@href')
    film_info = dict(zip(film_name, film_link))

    
    
    for i in film_info:
        #print(f'电影名称： {i}\t\t电影链接： {film_info[i]}')
        text = f'电影名称： {i}\t\t电影链接： {film_info[i]}\r\n'
        #print(text)
        with open('top250.txt','a+') as f:
            f.write(text)

            

if __name__ == '__main__':
    urls = tuple(f'https://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(10))
    for page in urls:
        get_movies_list(page)
        sleep(5)