import requests
import pandas as pd
import time
import random
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

fashion = ['167','168','169','170','173','174','176','177','178','179','181','185','186','189']
care = ['190','191','192','193','194','195','196','197','198','199','200','201','202']
digit = ['089','152','153','151','204','205','206','208','094','097','209','210','212','096','098','213','211','088','214']
interior = ['100','102','103','109','113','101','105','107','110','154','112','104','106','108','111','114']
kid = ['115','116','117','118','119','120','121','122','123','124']
food = ['145','159','160','146','147','149','148','025','026','150','023']
sports = ['027','028','029','161','053','163','164','030','034','031','035']
life = ['055','061','062','076','158','078','165','054','156','155']
culture = ['082','011','086']

dataArray = [fashion,care,digit,interior,kid,food,sports,life,culture]


for idx, i in enumerate(dataArray):
    result = []
    for idx2, val in enumerate(i):
        for j in range(1,51):
            print(str(idx-3) + "/" + str(len(dataArray)) + "번째 카테고리의 " + str(idx2+1) + "/" + str(len(i)) +  " 번째 세부카테고리의 " + str(j) + "페이지")
            req = requests.get('https://search.shopping.naver.com/search/category.nhn?pagingIndex='+str(j)+'&pagingSize=40&viewType=list&sort=rel&cat_id=50000'+val+'&frm=NVSHPAG', headers=headers)
            soup = BeautifulSoup(req.text, 'html.parser')
            information_list = soup.select('div > a.tit')
            for info in information_list:
                result.append(info.text.strip())
            time.sleep(0.5)
        print("세부 카테고리 하나 완료")
    table = pd.DataFrame(result, columns=['name'])
    table.to_csv('./'+str(idx)+'.csv', encoding='utf-8', mode='w')
    print("카테고리 하나 완료")
    time.sleep(random.randrange(3,8))
