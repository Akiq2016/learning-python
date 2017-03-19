# -*- coding: utf-8 -*-
'''
@author: Aki
'''

# 有结果：
# id="container" > ol li a
# 有下一页：
# document.getElementById('nextPage')

import requests as req
from bs4 import BeautifulSoup
from pprint import pprint
import re

def main():
  keyword = 'cat'
  initPage = '1'
  getIcon(keyword, initPage)

def getIcon(keyword, pagenum):
  res = req.get("http://www.easyicon.net/iconsearch/" + keyword + "/" + pagenum)
  cur_str = BeautifulSoup(res.text, 'html.parser')
  content = cur_str.find(id="container") # 搜索结果
  if content:
    for index, item in enumerate(content.find_all("div" , "k_left")): # div.k_left 包含png, ico, icns三条可下载链接
      url = item.find(href=re.compile("png")).get('href') 
      r = req.get(url)
      with open("icon/%(page)s-%(num)d.png" % {'page': pagenum, 'num': index}, "wb") as code: # 将图片存入当前路径中的icon目录下
        code.write(r.content)
    print('第%s页下载完成' % pagenum)
    nextPage = cur_str.find(id="nextPage")
    if nextPage: # 存在下一页
      nextnum = str(int(pagenum)+1)
      print('准备请求第%s页' % nextnum)
      getIcon(keyword, nextnum)
    else:
      print('该关键词下载完成')
  else:
    print('Try another keyword / 换个关键词试试吧。')

main()