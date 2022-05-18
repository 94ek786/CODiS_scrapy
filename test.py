import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome(executable_path='C:\\driver\\chromedriver.exe')
browser.get('https://e-service.cwb.gov.tw/HistoryDataQuery/')

time.sleep(3)


time.sleep(100)