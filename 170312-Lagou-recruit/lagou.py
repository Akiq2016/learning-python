# -*- coding: utf-8 -*-
'''
@author: Aki
'''
# curl 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false' 
# -H 'Cookie: user_trace_token=20170211192118-5b6790b2842b4e6582a8e65aff533347; LGUID=20170211192118-35953aa1-f04c-11e6-a378-525400f775ce; index_location_city=%E5%B9%BF%E5%B7%9E; JSESSIONID=5A5B992A6F53F4B6A0275CC2B3317991; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_search; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1486812082,1489155691; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1489309203; _gat=1; LGSID=20170312164502-2ed82ffe-0700-11e7-93bb-525400f775ce; LGRID=20170312170002-474ec9f2-0702-11e7-928e-5254005c3644; _ga=GA1.2.1045120157.1486812081; SEARCH_ID=2f42a6953fec4e4bb843c4dbaec3da75' 
# -H 'Origin: https://www.lagou.com' 
# --data 'first=true&pn=1&kd=%E5%89%8D%E7%AB%AF' 

import requests as req
import pandas as pd
import json
from pprint import pprint

def get_post(page, keyword):
  header = {
    'Origin': 'https://www.lagou.com',
    'Cookie': 'user_trace_token=20170211192118-5b6790b2842b4e6582a8e65aff533347; LGUID=20170211192118-35953aa1-f04c-11e6-a378-525400f775ce; index_location_city=%E5%B9%BF%E5%B7%9E; JSESSIONID=5A5B992A6F53F4B6A0275CC2B3317991; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_search; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1486812082,1489155691; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1489309203; _gat=1; LGSID=20170312164502-2ed82ffe-0700-11e7-93bb-525400f775ce; LGRID=20170312170002-474ec9f2-0702-11e7-928e-5254005c3644; _ga=GA1.2.1045120157.1486812081; SEARCH_ID=2f42a6953fec4e4bb843c4dbaec3da75'
  }
  param = {
    'city': '广州',
    'needAddtionalResult': 'false'
  }
  if page == 1:
    status = 'true'
  else:
    status = 'false'
  form = {
    'first': status,
    'pn': page,
    'kd': keyword
  }
  r = req.post("https://www.lagou.com/jobs/positionAjax.json", params=param, headers=header, data=form)
  res = json.loads(r.text)
  arrResult = res['content']['positionResult']['result']
  # pprint(arrResult) # <class 'list'> what we want
  return arrResult

def main():
  result = []
  n = 1
  while n<30:
    result += get_post(n, '前端')
    n = n + 1
  # pprint(result)
  df = pd.DataFrame(result)
  df.to_excel('lagou.xlsx', sheet_name='test1')
main()


# from urllib import request, parse, error

# def get_post(url, pn, key): # 链接, 第几页, 关键词
#   header = {
#     'Origin': 'https://www.lagou.com',
#     'Cookie': 'user_trace_token=20170211192118-5b6790b2842b4e6582a8e65aff533347; LGUID=20170211192118-35953aa1-f04c-11e6-a378-525400f775ce; index_location_city=%E5%B9%BF%E5%B7%9E; TG-TRACK-CODE=search_code; JSESSIONID=5A5B992A6F53F4B6A0275CC2B3317991; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1486812082,1489155691; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1489290566; LGSID=20170312114926-e34a2dbe-06d6-11e7-8fec-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E5%2589%258D%25E7%25AB%25AF%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E5%2589%258D%25E7%25AB%25AF%3Fcity%3D%25E5%25B9%25BF%25E5%25B7%259E%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; LGRID=20170312114926-e34a2f2f-06d6-11e7-8fec-525400f775ce; _ga=GA1.2.1045120157.1486812081; SEARCH_ID=8c25ed6d640140c7ae0daa3a9832c4e8',
#   }
#   if pn == 1:
#     status = 'true'
#   else:
#     status = 'false'

#   data = parse.urlencode([ ('first', status), ('pn', pn), ('kd', key) ]).encode('utf-8')
#   req  = request.Request(url, data, header)
#   try: 
#     res = request.urlopen(req)
#     page = res.read()
#     print(page.decode('utf-8'))
#   except error.HTTPError as e:
#     print(e.code, e.headers)

# def main():
#   url = r'https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'
#   get_post(url, 1, '前端')

# main()