import time
import allure
from base import driver
from pathlib import Path

@allure.step("Take Screenshot")
def takeScreenshot(path: str, name: str):
    pathname = path + '/' + name
    try:
        # Giving time for any quick animations to complete
        time.sleep(1)
        driver.save_screenshot(pathname)
        allure.attach.file(pathname, name, attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        print(e)