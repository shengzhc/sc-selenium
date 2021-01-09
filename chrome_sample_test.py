import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.google.com/')
breakpoint()
print(driver.page_response)
print(driver)
print(dir(driver))
time.sleep(5)
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromDriver')
search_box.submit()
time.sleep(5)
driver.quit()
