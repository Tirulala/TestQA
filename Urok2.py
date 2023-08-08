from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "https://www.provartesting.com/contact/?utm_source=google&utm_medium=cpc&utm_campaign=uk_competitor&gclid=Cj0KCQjwz8emBhDrARIsANNJjS5nGD0ripp8PE5713StPCS5Ay_rdYqVyo6yxC6-LmVHKhwc618lwqwaAoOeEALw_wcB"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(3)

select = Select(browser.find_element(By.XPATH, '//*[@id="input_11_10"]'))
select.select_by_value("Aruba") # ищем элемент

# button = browser.find_element(By.XPATH, '/html/body/div/form/button')
# button.click()

time.sleep(5)
browser.quit()