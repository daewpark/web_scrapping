from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import time

import urllib.request
from bs4 import BeautifulSoup
import re

options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path="./chromedriver", options=options)

url = "https://www.ep.go.kr/CmsWeb/viewPage.req?idx=PG0000001180"

driver.get(url)

time.sleep(1)

search = driver.find_element_by_name("searTot")
search.send_keys("원아모집")
search.submit()

driver.switch_to.window(driver.window_handles[-1])
search_html = driver.page_source

soup = BeautifulSoup(search_html,'html.parser')
title = soup.find_all(class_='sr_web')
print(title)

import pandas as pd

result_list = []

for i in title :
    ititle = i.attrs['title']
    ilink = i.attrs['href']
    result_list.append([ititle,ilink])

df = pd.DataFrame(result_list, columns = ["title","link"])
print(df)
