from selenium.webdriver.remote.webelement import WebElement

class Verifications:
    def verifyElementDisplayed(element: WebElement):
        assert element.is_displayed()  
    
    def verifyElementAttribute(element: WebElement, attribute: str, expected_value: str):
        assert element.get_attribute(attribute) == expected_value
    