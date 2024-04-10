import allure
from fixtures.tokensFarmSetup import tokens_farm_setup
from base import screenshotsFolder
from commonOps import takeScreenshot
from selenium.webdriver.remote.webelement import WebElement

from extensions.ui_actions import UI_Actions
from extensions.verifications import Verifications
from locators.tokens_farm_locators import tokens_farm_locators

@allure.title("Verify TokensFarm dropdown")
@allure.description("Should expand token chain dropdown")
@allure.link("https://staging.tokensfarm.com/create#/staking", name="TokensFarm Website")
def test_tokens_farm(tokens_farm_setup):
    
    # # Tried to solve test flakiness by closing the connect wallet modal that not always appears
    # if len(driver.find_elements(By.CSS_SELECTOR, tokens_farm_locators.wallet_connect_close_modal)) > 0:
    #     wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, tokens_farm_locators.wallet_connect_buttons)))
    #     close_connect_wallet_modal: WebElement = UI_Actions.getVisibleElement(tokens_farm_locators.wallet_connect_close_modal)
    #     UI_Actions.click(close_connect_wallet_modal)
    #     print("\nClosed connect wallet modal")
    # else:
    #     print("\nNo connect wallet modal found")
    
    dropdown: WebElement = UI_Actions.getVisibleElement(tokens_farm_locators.token_chain_dropdown)
    UI_Actions.click(dropdown)
    
    input: WebElement = UI_Actions.getElement(tokens_farm_locators.expanded_dropdown)
    Verifications.verifyElementAttribute(input, 'aria-expanded', 'true')
    
    takeScreenshot(screenshotsFolder, "token_chain_dropdown.png")
