from selenium import webdriver
from selenium.webdriver.chrome.options import Options

l = ['none', 'eager', 'normal']

for s in l:
    try:
        options = Options()
        options.page_load_strategy = s
        driver = webdriver.Chrome(options=options)
        driver.get("http://www.google.com")
        with open(f"download/google-{s}.html", "w") as f:
            f.write(driver.page_source)
    except Exception:
        print("Error")
    finally:
        driver.quit()
