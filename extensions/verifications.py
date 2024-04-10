from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from commonOps import wait



class Verifications:
    def verifyElementDisplayed(element: WebElement):
        assert element.is_displayed()  
    
    def verifyElementAttribute(element: WebElement, attribute: str, expected_value: str):
        assert element.get_attribute(attribute) == expected_value
        
    def verifyElementAttributeDoesNotContain(element: WebElement, attribute: str, value: str):
        assert element.get_attribute(attribute).find(value) == -1
        
    def verifyInt(actual: int, expected: int):
        assert actual == expected  
    
    def verifyIntAbove(actual: int, expected: int):
        assert actual > expected  

    def verifyElementsNotFound(selector: str):
        try:
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
        except NoSuchElementException:
            pass