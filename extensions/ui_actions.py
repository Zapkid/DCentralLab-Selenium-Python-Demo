import allure
from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base import wait, action

class UI_Actions:
    
    @allure.step("Get element")
    def getElement(selector: str) -> WebElement:
        return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    
    @allure.step("Get elements")
    def getElements(selector: str) -> List[WebElement]:
        return wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))

    @allure.step("Get visible element")
    def getVisibleElement(selector: str) -> WebElement:
        return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
         

    @allure.step("Click element")
    def click(element: WebElement):
        wait.until(EC.element_to_be_clickable(element))
        element.click()
        
    @allure.step("Hover on element & click")
    def hoverAndClick(element: WebElement):
        action.move_to_element(element).click().perform()