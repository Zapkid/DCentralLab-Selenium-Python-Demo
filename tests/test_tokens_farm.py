import allure
from fixtures.tokensFarmSetup import tokens_farm_setup
from utils.base import screenshotsFolder
from utils.screenshot import takeScreenshot
from selenium.webdriver.remote.webelement import WebElement

from extensions.ui_actions import UI_Actions
from extensions.verifications import Verifications
from locators.tokens_farm_locators import tokens_farm_locators

@allure.title("Verify TokensFarm dropdown")
@allure.description("Should expand token chain dropdown")
@allure.link("https://staging.tokensfarm.com/create#/staking", name="TokensFarm Website")
def test_tokens_farm(tokens_farm_setup):
    
    dropdown: WebElement = UI_Actions.getVisibleElement(tokens_farm_locators.token_chain_dropdown)
    UI_Actions.click(dropdown)
    
    input: WebElement = UI_Actions.getElement(tokens_farm_locators.expanded_dropdown)
    Verifications.verifyElementAttribute(input, 'aria-expanded', 'true')
    
    takeScreenshot(screenshotsFolder, "token_chain_dropdown.png")
