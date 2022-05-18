import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time
import json

def is_float(value):
  try:
    float(value)
    return True
  except:
    return False

a_err = 'https://e-service.cwb.gov.tw/HistoryDataQuery/MonthDataController.do?command=viewMain&station=466921&stname=%25E8%2587%25BA%25E5%258C%2597(%25E5%25B8%25AB%25E9%2599%25A2)&datepicker=2022-05&altitude=6.1m'
a_yas = 'https://e-service.cwb.gov.tw/HistoryDataQuery/MonthDataController.do?command=viewMain&station=466910&stname=%25E9%259E%258D%25E9%2583%25A8&datepicker=2022-05&altitude=0m'

browser = webdriver.Chrome(executable_path='C:\\driver\\chromedriver.exe')
browser.get(a_err)
time.sleep(2)
i = browser.find_element_by_xpath('//*[@id="MyTable"]/tbody/tr[4]/td[8]')
if(is_float(i.text)):
    print('y')
else:
    print('n')

time.sleep(50)