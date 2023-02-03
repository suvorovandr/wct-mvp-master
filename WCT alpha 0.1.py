## Author: Andrey Suvorov
## Date: 15/01/2023
import sqlite3 as sql
import requests
from bs4 import BeautifulSoup
import csv
import os.path
from win32.win32api import MessageBox


store_domain = "https://www.mechta.kz/api/v1/product/"

con = sql.connect('region.db')

if os.path.isfile('region.db'):
    print ("Database File exist | 数据库连接成功")
else:
    print ("Database File does not exist | 无数据库可连接")
    input("")
    ##con = sql.connect('region.db')
    ##with con:
     ##   con.execute("""
     ##   CREATE TABLE USER (
     ##       region TEXT,
     ##       client TEXT,
    ##        link STRING PRIMARY KEY); """)
   ## con.commit()


def selectdata():
    cursor = con.cursor()
    cursor.execute('SELECT link FROM USER WHERE region = "KZ" AND client = "mechta"')
    row = cursor.fetchall()
    for i, rows in enumerate(row):
        row[i] = rows[0]
    return row


def parse_page(addr_list):
    print("欢迎使用HONOR WCT 工具 alpha版(kz) | Welome to use Honor WCT Kazakhstan prototype")
    parse_index = 0
    csv_report = open('price_monitoring.csv', 'w', encoding='cp1251')
    write_file = csv.writer(csv_report)
    for default_addr in addr_list:
        parse_index += 1
        print("以解析" + parse_index + "/" + addr_list(len) + "设备信息")
        print("already parsed" + parse_index + "/" + addr_list(len) + "devices")
        url = store_domain + default_addr[30:]
        page = requests.get(url)
        market_data = page.json()
        ## market_data = page.json()
        device_name = market_data['data'].get('name')
        ids = market_data['data'].get('id')
        api = "https://www.mechta.kz/api/v1/mindbox/actions/product"
        headers = {'Content-type': 'application/json'}
        page_json = requests.post(api, headers=headers, json={'product_ids': ids})
        json_data = page_json.json()
        base_price = json_data['data'].get('prices').get('base_price')
        discounted_price = json_data['data'].get('prices').get('discounted_price')
        bonus = json_data['data'].get('bonus')
        gift_data = json_data['data'].get('has_gift')
        gift_array = []
        if gift_data == True:
            gift_object = json_data['data'].get('gifts')
            ## print(gift_object)
            key = list(gift_object.keys())
            for i in range(len(key)):
                gift_details = gift_object.get(key[i])
                for i, keys in enumerate(gift_details):
                    keys[i] = gift_details[0]
                    gift_name = keys['name']
                    gift_array.append(gift_name)
                    gift = requests.post(api, headers=headers, json={'product_ids': keys['id']})
                    gift_json = gift.json()
                try:
                    gift_base_price = gift_json['data'].get('prices').get('base_price')
                    ## print(device_name, base_price, discounted_price, bonus, gift_array, gift_base_price)
                    data = [device_name, base_price, discounted_price, bonus, gift_array, gift_base_price]
                    write_file.writerow(data)
                except(AttributeError): continue
        data = [device_name, base_price, discounted_price, bonus, gift_array]
        write_file.writerow(data)
    csv_report.close()
    print("CSV报告已导出 | CSV file already Ok :)")
            ##data = [device_name, base_price, discounted_price, bonus, gift_array]
            ##write_file.writerow(data)
            ## print(gift_object)
        ## data = [device_name, base_price, discounted_price, bonus, gift_array, gift_base_price]
        ## write_file.writerow(data)

parse_page(selectdata())
input("请按enter将退出工具 | please press enter to exit tool")
## parse_page(addr_list=["https://www.mechta.kz/product/telefon-sotovyy-vivo-y16-332gb-stellar-black-2204/", "https://www.mechta.kz/product/telefon-sotovyy-vivo-y16-332gb-stellar-black-2204/"])
        ## return(data)
        ## json_to_csv(data)
## parse_page(addr_list=["https://www.mechta.kz/product/telefon-sotovyy-xiaomi-redmi-note-11-pro-8128gb-graphite-gray/", "https://www.mechta.kz/product/telefon-sotovyy-honor-x6-464gb-midnight-black/"])



## price = jsonDic.get('price')
## price_mindbox = data_mindbox.get('prices')















