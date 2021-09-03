from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://app.slack.com/client/TEAK2910W/CEA8SM6JK')
while True:
    time.sleep(10)
    driver.refresh()
driver.quit()