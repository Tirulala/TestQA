from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

n1 = browser.find_element(By.XPATH, '//*[@id="num1"]').text
n1 = int(n1)
n2 = browser.find_element(By.XPATH, '//*[@id="num2"]').text
n2 = int(n2)
value = str(n1 + n2)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_visible_text(value) # ищем элемент

button = browser.find_element(By.XPATH, '/html/body/div/form/button')
button.click()

time.sleep(5)
browser.quit()