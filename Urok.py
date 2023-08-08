from selenium.webdriver.common.by import By
from selenium import webdriver
import time


link = "https://paulradzkov.com/"
browser = webdriver.Chrome()
browser.get(link)

button2 = browser.find_element(By.XPATH, '/html/body/header/div[2]/nav/a[4]')
button2.click()

input1 = browser.find_element(By.XPATH, '//*[@id="gsc-i-id1"]')
input1.send_keys(55555)
time.sleep(3)

button2 = browser.find_element(By.XPATH, '//*[@id="___gcse_0"]/div/div/form/table/tbody/tr/td[2]/button')
button2.click()

info1 = browser.find_element(By.XPATH, "/html/body/header/div[1]/a/span[2]/span")
info1 = info1.text
assert 'Павел Радьков' == info1
print('YES')

link = "https://yohoho.cc/"
browser = webdriver.Chrome()
browser.get(link)

movie = browser.find_element(By.XPATH, '//*[@id="search-title"]')
movie.send_keys(666)

button_movie = browser.find_element(By.XPATH, '//*[@id="search"]')
button_movie.click()

time.sleep(5)
browser.quit()