from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.get("http://www.google.com")
with open(f"download/google-{options.page_load_strategy}.html", "w") as f:
    f.write(driver.page_source)

driver.quit()
