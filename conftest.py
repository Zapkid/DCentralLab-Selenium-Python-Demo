from utils.base import driver
import time
import allure


@allure.step("Session Start")
def pytest_sessionstart(session):
    driver.maximize_window()
    
    # Explicitly waiting for page to load the DOM
    # Not good practice, should be replaced with better waiting for full page load
    time.sleep(5)

@allure.step("Session Finish")
def pytest_sessionfinish(session, exitstatus):
    driver.quit()