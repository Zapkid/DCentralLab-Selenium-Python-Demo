from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
action = ActionChains(driver)

screenshotsFolder: str = 'assets/screenshots'
