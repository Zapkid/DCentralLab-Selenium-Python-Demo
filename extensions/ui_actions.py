from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from commonOps import wait, action

class UI_Actions:
    
    def getElement(selector: str) -> WebElement:
        return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    
    def getElements(selector: str) -> List[WebElement]:
        return wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))

    def getVisibleElement(selector: str) -> WebElement:
        return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
         

    def click(element: WebElement):
        wait.until(EC.element_to_be_clickable(element))
        element.click()
        
    def hoverAndClick(element: WebElement):
        action.move_to_element(element).click().perform()