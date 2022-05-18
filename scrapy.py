import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time
import json
import copy

time_range = [[2022, 5], [2020, 1]]
M_T = ['00','01','02','03','04','05','06','07','08','09','10','11','12']

def is_float(value):
  try:
    float(value)
    return True
  except:
    return False

def sc(i):
    loop_time = copy.deepcopy(time_range[0])
    while(loop_time != time_range[1]):
        browser.get('https://e-service.cwb.gov.tw/HistoryDataQuery/MonthDataController.do?command=viewMain&station=' + str(i[0]) + '&stname=%25E9%259E%258D%25E9%2583%25A8&datepicker=' + str(loop_time[0]) + '-' + M_T[loop_time[1]] + '&altitude=0m')
        time.sleep(3)
        #判斷該月第一天是否有資料
        if(is_float(browser.find_element_by_xpath('//*[@id="MyTable"]/tbody/tr[4]/td[8]').text)):
            browser.find_element_by_id('downloadCSV').click()
        else:
            #沒資料的話回傳
            txt = i[0] + i[1] + ' stop at ' + str(loop_time)
            return txt
            #減少
        if(loop_time[1] == 1):
            loop_time[0] -= 1
            loop_time[1] = 12
        else:
            loop_time[1] -= 1

    txt = i[0] + i[1] + ' good'
    return txt

#borwser
browser = webdriver.Chrome(executable_path='C:\\driver\\chromedriver.exe')
browser.maximize_window()
time.sleep(20)

#讀取station_id.json
with open('data.json','r') as jsonfile:
    stationId = json.load(jsonfile)
jsonfile.close()

s_log = []
with open('log.json','w+') as jsonfile:
    s = jsonfile
    jsonfile.close()
s_log.append(s)

for loop in stationId:
    try:
        stxt = sc(loop)
        s_log.append(stxt)
        print(stxt)
        stationId = stationId[1:]
    except:
        with open('unfinish.json','w') as unF:
            json.dump(stationId, unF)
            unF.close()
        with open('log.json','w+') as jsonfile:
            print(s_log)
            json.dump(s_log, jsonfile)
            jsonfile.close()
        break
print(s_log)









browser.close()