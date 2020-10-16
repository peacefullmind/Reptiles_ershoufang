#http://esf.0515fc.cn/esf-1-1-0-0-0-0-0-0-0-0-.html 网址
import numpy as np
import requests
import time
import xlwt
from bs4 import BeautifulSoup
file =xlwt.Workbook() #新建一个excel
table=file.add_sheet('from鹤鸣亭')

table_row=0#这是行数，从0行开始写
table.write(table_row, 0, '名称')  # 将,,写入
table.write(table_row, 1, '面积')  # 将,,写入
table.write(table_row, 2, '户型')  # 将,,写入
table.write(table_row, 3, '楼层')  # 将,,写入
table.write(table_row, 4,'装修')  # 将,,写
table_row = table_row + 1
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'
    }
page=1
while page<11:
    url = "http://esf.0515fc.cn/esf-" + str(page) + "-1-0-0-0-0-0-0-0-0-.html"
    r = requests.get(url, headers=headers)
    # print(r.text)
    # text = r.text.encode('iso-8859-1').decode('gbk')
    bs = BeautifulSoup(r.text, "html.parser")
    homes = bs.find('ul', attrs={'class': 'ershou_list'}).find_all('li')
    # for i in homes:

    for i in homes:
        print(type(i))
        home_title = i.find('a', attrs={'class': 'title fl ellipsis'}).text
        print(home_title)
        table.write(table_row, 0, home_title)  # 将,,写入

        cont1 = i.find_all('div', attrs={'class': 'font'})[0].text
        cont2 = i.find_all('div', attrs={'class': 'font'})[2].text
        mianji = cont1.split('|')[0]
        mianji = "".join(mianji.split())
        print(mianji)
        table.write(table_row, 1, mianji)  # 将,,写入

        huxing = cont1.split('|')[1]
        huxing = "".join(huxing.split())
        print(huxing)
        table.write(table_row, 2, huxing)  # 将,,写入

        louceng = cont1.split('|')[2]
        louceng = "".join(louceng.split())
        print(louceng)
        table.write(table_row, 3, louceng)  # 将,,写入

        zhuangxiu = cont1.split('|')[3]
        zhuangxiu = "".join(zhuangxiu.split())
        print(zhuangxiu)
        table.write(table_row, 4, zhuangxiu)  # 将,,写
        table_row = table_row + 1
    page = page + 1



# print(cont1.split('|'))
file.save('二手房信息.xls')
