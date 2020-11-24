#!/usr/bin/env python
import os
import time

def showlog():
    # 格式化当前日期
    show_date = time.strftime('%Y%m%d', time.localtime())
    # 格式化当前时间
    show_time = time.strftime('%H-%M-%S', time.localtime()) + '.log'
    # 创建以当前日期命名的变量
    show_path = 'python-' + show_date
    # 进入对应的文件目录
    os.chdir('/Users/tristan/Documents/GitHub/Python005-01/week01/var/log')
    # 判断以当前日期命名的文件夹是否存在，存在时进入该文件目录下，不存在时创建文件夹，并进入其目录下
    if os.path.exists('/Users/tristan/Documents/GitHub/Python005-01/week01/var/log/'+show_path):
        os.chdir('/Users/tristan/Documents/GitHub/Python005-01/week01/var/log/'+show_path)
    else:
        os.mkdir(show_path)
        os.chdir('/Users/tristan/Documents/GitHub/Python005-01/week01/var/log/'+show_path)
    # 打开以当前时间命名的文件，对其进行写入操作
    log = open(show_time, 'w+')
    log.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    log.close()

if __name__ == '__main__':
    showlog()