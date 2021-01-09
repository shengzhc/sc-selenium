from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get("http://ff14fish.carbuncleplushy.com/")
el = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element(By.ID, "fishes"))
print(el)
driver.quit()
