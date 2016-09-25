from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
pollution_business = client['pollution_business']
enterprise_info = pollution_business['enterprise_info']

x = 0 #判断是否到最后一页
def get_every_info(channel,pages):
    page_url = '{}&cp={}'.format(channel,str(pages))
    wb_data = requests.get(page_url)
    wb_data.encoding = 'gb18030'
    soup = BeautifulSoup(wb_data.text, 'lxml',from_encoding='UTF-8')
    time.sleep(1)

    if soup.find(color="#CCCCCC",string="下一页 | 尾页 "):
        infos = soup.select('body > div:nth-of-type(6) > div > a')
        for each in infos:
            every_info = each.get_text()
            name = every_info.split(' 电话：')[0]
            tele = every_info.split(' 电话：')[1]
            enterprise_info.insert_one({'公司':name,'电话':tele,'所在行业':channel,'页码':pages})
            global x
            x = 1 #x=1说明已到达最后一页
    else:
        infos = soup.select('body > div:nth-of-type(6) > div > a')
        for each in infos:
            every_info = each.get_text()
            name = every_info.split(' 电话：')[0]
            tele = every_info.split(' 电话：')[1]
            enterprise_info.insert_one({'公司':name,'电话':tele,'所在行业':channel,'页码':pages})