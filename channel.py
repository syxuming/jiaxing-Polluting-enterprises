from bs4 import BeautifulSoup
import requests

##抓取所有行业链接
url  = 'http://www.socom.cn/zhejiang/jiaxing/'

def channel_extact():
    wb_data = requests.get(url)
    wb_data.encoding = 'gb18030'
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('body > div:nth-of-type(4) > div > a[class]')

    for title,link in zip(titles,titles):
        data = {
            'title': title.get_text(),
            'link': 'http://www.socom.cn' + title.get('href')
        }
        print(data)

##人工筛选污染行业
links = [
    'http://www.socom.cn/zhejiang/jiaxing/1111/',
    'http://www.socom.cn/zhejiang/jiaxing/1112/',
    'http://www.socom.cn/zhejiang/jiaxing/1114/',
    'http://www.socom.cn/zhejiang/jiaxing/1115/',
    'http://www.socom.cn/zhejiang/jiaxing/1214/',
    'http://www.socom.cn/zhejiang/jiaxing/1215/',
    'http://www.socom.cn/zhejiang/jiaxing/1216/',
    'http://www.socom.cn/zhejiang/jiaxing/1217/',
    'http://www.socom.cn/zhejiang/jiaxing/1218/',
    'http://www.socom.cn/zhejiang/jiaxing/1219/',
    'http://www.socom.cn/zhejiang/jiaxing/1220/',
    'http://www.socom.cn/zhejiang/jiaxing/1222/',
    'http://www.socom.cn/zhejiang/jiaxing/1223/',
    'http://www.socom.cn/zhejiang/jiaxing/1224/',
    'http://www.socom.cn/zhejiang/jiaxing/1225/',
    'http://www.socom.cn/zhejiang/jiaxing/1226/',
    'http://www.socom.cn/zhejiang/jiaxing/1227/',
    'http://www.socom.cn/zhejiang/jiaxing/1228/',
    'http://www.socom.cn/zhejiang/jiaxing/1229/',
    'http://www.socom.cn/zhejiang/jiaxing/1230/',
    'http://www.socom.cn/zhejiang/jiaxing/1231/',
    'http://www.socom.cn/zhejiang/jiaxing/1232/',
    'http://www.socom.cn/zhejiang/jiaxing/1233/',
    'http://www.socom.cn/zhejiang/jiaxing/1234/',
    'http://www.socom.cn/zhejiang/jiaxing/1235/',
    'http://www.socom.cn/zhejiang/jiaxing/1310/',
    'http://www.socom.cn/zhejiang/jiaxing/1311/',
    'http://www.socom.cn/zhejiang/jiaxing/1410/',
    'http://www.socom.cn/zhejiang/jiaxing/1412/',
    'http://www.socom.cn/zhejiang/jiaxing/1413/',
]

new_list = []

##网页地址转化(原地址没有显示全部信息)
def trans_links(url):
    code = url.split('/')[-2]
    new = 'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=' + str(code)
    new_list.append(new)

# for each in links:
#     trans_links(each)
#
# for i in new_list:
#     print(i)

channel_url = [
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1111',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1112',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1114',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1115',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1214',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1215',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1216',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1217',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1218',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1219',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1220',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1222',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1223',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1224',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1225',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1226',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1227',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1228',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1229',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1230',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1231',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1232',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1233',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1234',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1235',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1310',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1311',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1410',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1412',
    'http://www.socom.cn/company/company_list.jsp?locationId=3304&categoryId=1413',
]