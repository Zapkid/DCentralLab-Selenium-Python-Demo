import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
action = ActionChains(driver)

def takeScreenshot(pathname: str):
    try:
        # Giving time for any quick animations to complete
        time.sleep(1)
        driver.save_screenshot(pathname)
    except Exception as e:
        print(e)