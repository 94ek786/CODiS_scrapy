import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time
import json

time_range = [[2022, 5], [2020, 1]]
M_T = ['00','01','02','03','04','05','06','07','08','09','10','11','12']

def is_float(value):
  try:
    float(value)
    return True
  except:
    return False

def sc(i):
    loop_time = time_range[0]
    while(loop_time != time_range[1]):
        browser.get('https://e-service.cwb.gov.tw/HistoryDataQuery/MonthDataController.do?command=viewMain&station=' + str(i[0]) + '&stname=%25E9%259E%258D%25E9%2583%25A8&datepicker=' + str(loop_time[0]) + '-' + M_T[loop_time[1]] + '&altitude=0m')
        time.sleep(1)
        if(is_float(browser.find_element_by_xpath('//*[@id="MyTable"]/tbody/tr[4]/td[8]').text)):
            print(loop_time)
        else:
            txt = i[0] + i[1] + ' stop at ' + str(loop_time)
            return txt
        if(loop_time[1] == 1):
            loop_time[0] -= 1
            loop_time[1] = 12
        else:
            loop_time[1] -= 1

    txt = i[0] + i[1] + ' good'
    return txt
browser = webdriver.Chrome(executable_path='C:\\driver\\chromedriver.exe')

#讀取station_id.json
with open('station_id.json','r') as jsonfile:
    stationId = json.load(jsonfile)
jsonfile.close()

s_log = []

for loop in stationId:
    stxt = sc(loop)
    s_log.append(stxt)
    print(stxt)
print(s_log)


time.sleep(100)






# browser.close()