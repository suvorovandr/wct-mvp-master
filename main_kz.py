## Author: Andrey Suvorov
## Date: 03/02/2023
import sqlite3 as sql
import requests
import csv
import os.path


store_domain = "https://www.mechta.kz/api/v1/product/"
catalog_link = "https://www.mechta.kz/api/v1/catalog?section=smartfony&page=1&properties=&page_limit=24&cache_city=s1"



def db_check():
    if os.path.exists("region.db"):
        os.remove("region.db")
def db_create():
    con = sql.connect('region.db')
    with con:
        con.execute("""
        CREATE TABLE USER (
            region TEXT,
            client TEXT,
            link STRING PRIMARY KEY); """)
    con.commit()
def db_write_data(full_link_attribut):
    con = sql.connect('region.db')
    cursor = con.cursor()
    cursor.execute(("""
        INSERT or REPLACE INTO USER (region, client, link) 
        VALUES 
        (?, ?, ?)
        """), ("KZ", "mechta", full_link_attribut))
    con.commit()
    cursor.close()


def get_links_to_db():
    db_check()
    db_create()
    get_catalog_jsons = requests.get(catalog_link)
    json = get_catalog_jsons.json()
    device_count = json['data'].get('all_items_count')
    print("All need to parse: "+ str(device_count) + " devices")
    page_count = json['data'].get('page_items_count')
    device_sum = 0
    for i in range(page_count + 1):
        catalog_link_auto = "https://www.mechta.kz/api/v1/catalog?section=smartfony&page="+str(i)+"&properties=&page_limit="+str(page_count)+"&cache_city=s1"
        items_json = requests.get(catalog_link_auto).json()
        device_code = items_json['data'].get('items')
        for i in range(len(device_code)):
            link_attribut = device_code[i]['code']
            full_link_attribut = "https://www.mechta.kz/product/" + link_attribut
            db_write_data(full_link_attribut)
            ## print(type(device_code[i]))
            ##for i, code in enumerate(items_dic):
                    ##code[i] = items_dic[0]
                   ## print(code['code'])
            device_sum = device_sum + 1
    print(device_sum)

print("Welcome to use Honor WCT Kazakhstan prototype")
print("Author: Andrey Suvorov (C) Honor Devices")

def selectdata():
    con = sql.connect('region.db')
    cursor = con.cursor()
    cursor.execute('SELECT link FROM USER WHERE region = "KZ" AND client = "mechta"')
    row = cursor.fetchall()
    for i, rows in enumerate(row):
        row[i] = rows[0]
    return row

def parse_page(addr_list):
    print("Selected region: KZ")
    print("Selected client: Mechta.kz")
    parse_index = 0
    for default_addr in addr_list:
        parse_index += 1
        print("already parsed " + str(parse_index) + " / " + str(len(addr_list)) + " devices", end ='\r')
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
                    writer.writerow(data)
                except(AttributeError): continue
        data = [device_name, base_price, discounted_price, bonus, gift_array]
        writer.writerow(data)
    print("CSV file already Ok :)                                             ")
            ##data = [device_name, base_price, discounted_price, bonus, gift_array]
            ##write_file.writerow(data)
            ## print(gift_object)
        ## data = [device_name, base_price, discounted_price, bonus, gift_array, gift_base_price]
        ## write_file.writerow(data)

headers_list = ["Device name", "Base price", "Discout", 'Bonus', "Gift_Details", "Gift_value"]

with open ('price_monitoring.csv', 'a', newline = '', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers_list)
    get_links_to_db()
    parse_page(selectdata())
input()















