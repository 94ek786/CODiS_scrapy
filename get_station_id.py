import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import json

browser = webdriver.Chrome(executable_path='C:\\driver\\chromedriver.exe')
browser.get('https://e-service.cwb.gov.tw/HistoryDataQuery/')
time.sleep(3)
#取得縣市數量
select_city = Select(browser.find_element_by_id('stationCounty'))
city_len = len(select_city.options)

station_data = []

for loop in range(city_len):
    #選縣市
    select_city.select_by_index(loop)
    time.sleep(1)
    #取stationId與名稱
    s = browser.find_element_by_id('station')
    for loop in s.get_attribute('innerHTML').split('<option value="')[1:]:
        i = loop.split('">')
        station_data.append([i[0], i[1].split('</option>')[0]])
#存id資料
with open('station_id.json','w') as jsonfile:
    json.dump(station_data, jsonfile)
    