import allure
from selenium.webdriver.remote.webelement import WebElement

class Verifications:
    @allure.step("Verify Element Displayed")
    def verifyElementDisplayed(element: WebElement):
        assert element.is_displayed()  
    
    @allure.step("Verify Element Attribute")
    def verifyElementAttribute(element: WebElement, attribute: str, expected_value: str):
        assert element.get_attribute(attribute) == expected_value
        
    @allure.step("Verify Element Attribute Does Not Contain")
    def verifyElementAttributeDoesNotContain(element: WebElement, attribute: str, value: str):
        assert element.get_attribute(attribute).find(value) == -1

    @allure.step("Verify Int Above")
    def verifyIntAbove(actual: int, expected: int):
        assert actual > expected  