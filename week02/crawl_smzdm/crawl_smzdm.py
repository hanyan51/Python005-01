#!usr/bin/env python

import requests
from time import sleep
from lxml import etree

def get_caizhuang_list(caizhuang_url):
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    header = {'user-agent': ua}

    response = requests.get(caizhuang_url, headers = header)

    selector = etree.HTML(response.text)
    caizhuang_name = selector.xpath('//div[@class = "feed-content"]/h5/a/text()')
    caizhuang_price = selector.xpath('//div[@class = "feed-content"]/div[1]/a/text()')

    caizhuang_info = dict(zip(caizhuang_name, caizhuang_price))
    for i in caizhuang_info:
        text = f'彩妆名称： {i}\r\n价格：{caizhuang_info[i].strip()}\r\n'
        with open('CaiZhuang_list.txt', 'a+') as f:
            f.write(text)

if __name__ == '__main__':
    urls = tuple(f'https://wiki.smzdm.com/caizhuangchanpin/p{i+1}'for i in range(1380))
    for page in urls:
        get_caizhuang_list(page)
        sleep(5)