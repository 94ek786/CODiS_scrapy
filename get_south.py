import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time
import json

city = ['臺南市', '高雄市', '屏東縣']
s_ = []

def Fstation(val):
    station_data = []
    select_city = Select(browser.find_element_by_id('stationCounty'))
    select_city.select_by_value(val)

    s = browser.find_element_by_id('station')
    for loop in s.get_attribute('innerHTML').split('<option value="')[1:]:
        i = loop.split('">')
        station_data.append([i[0], i[1].split('</option>')[0]])
        s_.append([i[0], i[1].split('</option>')[0]])
    return station_data


browser = webdriver.Chrome(executable_path='C:\\driver\\chromedriver.exe')
browser.get('https://e-service.cwb.gov.tw/HistoryDataQuery/')
time.sleep(3)

data = []
for loop in city:
    data.append(Fstation(loop))


with open('south_station.json','w+') as jsonfile:
    json.dump(data, jsonfile)
jsonfile.close()

with open('data.json','w+') as jsonfile:
    json.dump(s_, jsonfile)
jsonfile.close()