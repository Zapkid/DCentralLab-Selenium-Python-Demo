from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

def takeScreenshot(pathname: str):
    try:
        driver.save_screenshot(pathname)
    except Exception as e:
        print(e)