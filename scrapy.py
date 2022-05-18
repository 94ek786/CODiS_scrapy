import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time

loop_city = 
loop_station = 0
browser = webdriver.Chrome(executable_path='C:\\driver\\chromedriver.exe')
browser.get('https://e-service.cwb.gov.tw/HistoryDataQuery/')
time.sleep(3)
select_city = Select(browser.find_element_by_id('stationCounty'))
city_len = len(select_city.options)

while(loop_city < city_len):
    browser.get('https://e-service.cwb.gov.tw/HistoryDataQuery/')
    time.sleep(3)
    #選擇縣市
    select = Select(browser.find_element_by_id('stationCounty'))
    select.select_by_index(loop_city)
    #選擇月報表
    select = Select(browser.find_element_by_id('datatype'))
    select.select_by_index(1)
    #選日期
    browser.find_element_by_id('datepicker').send_keys('2022-05')
    browser.find_element_by_id('doquery').click()
    time.sleep(10)
    loop_city += 1
    print(loop_city)
    

time.sleep(100)






# browser.close()