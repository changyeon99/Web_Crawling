import csv
from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
#browser.set_window_size(400,600)

# 1. 페이지 이동
url = 'https://www.google.com/'
browser.get(url)
time.sleep(0.5)


# 2. 업종 검색
element = browser.find_element(By.NAME, 'q')
element.send_keys("음식료품")
element.submit()
time.sleep(0.5)

# 3. 뉴스 항목 클릭 ( 뉴스 위치는 다르기 때문에 xpath 안됨)
news = browser.find_element(By.LINK_TEXT, "뉴스")
news.click()
time.sleep(1)

# 4. 도구 항목 클릭
tool1 = browser.find_element(By.XPATH, '//*[@id="hdtb-tls"]')
tool1.click()
time.sleep(1)

# 5. 최근 항목 클릭
tool2 = browser.find_elements(By.CLASS_NAME, 'hdtb-mn-hd')
tool2[1].click()
time.sleep(1)

# 6. 기간 설정 클릭
period = browser.find_element(By.XPATH, '//*[@id="lb"]/div/g-menu/g-menu-item[8]/div/div/span')
period.click()
time.sleep(1)

# 7. 기간 설정 후 실행
start = browser.find_element(By.CLASS_NAME, 'OouJcb')
start.send_keys('01/2019')
end = browser.find_element(By.CLASS_NAME, 'rzG2be')
end.send_keys('01/2019')
time.sleep(1)
search = browser.find_element(By.XPATH, '//*[@id="T3kYXe"]/g-button')
search.click()
time.sleep(1)

# 



browser.quit()
