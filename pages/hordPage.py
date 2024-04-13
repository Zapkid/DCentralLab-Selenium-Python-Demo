import allure
from utils.base import screenshotsFolder
from utils.screenshot import takeScreenshot
from selenium.webdriver.remote.webelement import WebElement

from extensions.ui_actions import UI_Actions
from extensions.verifications import Verifications
from locators.hord_locators import hord_locators

# Can be moved to hordBase.py
sidebarExpandedClass: str = 'sidebar-expanded'

class HordPage:
    
    @allure.step("Verify Sidebar Toggled State")
    def verifySidebarToggledState(captureScreenshot = False):
        sidebarExpanded = HordPage.getSidebar().get_attribute('class').find(sidebarExpandedClass) != -1
        if sidebarExpanded:
            HordPage.verifySidebarExpanded()
            if captureScreenshot:
                takeScreenshot(screenshotsFolder, "hord_sidebar_expanded.png")
        else:
            collapsedSidebarElements = UI_Actions.getElements(hord_locators.collapsed_sidebar_items)
            Verifications.verifyElementsDoNotHaveAttribute(collapsedSidebarElements, sidebarExpandedClass)
            if captureScreenshot:
                takeScreenshot(screenshotsFolder, "hord_sidebar_collapsed.png")

    @allure.step("Toggle Sidebar")
    def toggleSidebar():
        UI_Actions.hoverAndClick(HordPage.getSidebarToggle())
            
    @allure.step("Get Sidebar")
    def getSidebar() -> WebElement:
        return UI_Actions.getElement(hord_locators.sidebar)

    @allure.step("Get Sidebar Toggle")
    def getSidebarToggle() -> WebElement:
        return UI_Actions.getElement(hord_locators.sidebar_toggler)

    @allure.step("Verify Sidebar Expanded")
    def verifySidebarExpanded():
        expanded_sidebar_items: WebElement = UI_Actions.getElements(hord_locators.expanded_sidebar_items)
        Verifications.verifyIntAbove(len(expanded_sidebar_items), 0)