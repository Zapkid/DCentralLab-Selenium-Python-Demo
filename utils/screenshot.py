import time
import allure
from utils.base import driver

@allure.step("Take Screenshot")
def takeScreenshot(path: str, name: str):
    pathname = path + '/' + name
    save_screenshot(pathname)
    attach_to_allure_report(name, pathname)

def attach_to_allure_report(name, pathname):
    b = convert_to_byte_array(pathname)   
    allure.attach(b, name, attachment_type=allure.attachment_type.PNG)

def convert_to_byte_array(pathname):
    with open(pathname, "rb") as image:
        stream = image.read()
        bytes = bytearray(stream)
    return bytes

def save_screenshot(pathname):
    try:
        # Giving time for any quick animations to complete
        time.sleep(1)
        driver.save_screenshot(pathname)
    except Exception as e:
        print(e)