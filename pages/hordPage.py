from commonOps import takeScreenshot
from selenium.webdriver.remote.webelement import WebElement

from extensions.ui_actions import UI_Actions
from extensions.verifications import Verifications
from locators.hord_locators import hord_locators

class HordPage:
    def verifySidebarToggledState(captureScreenshot = False):
        sidebar = HordPage.getSidebar() 
        if (sidebar.get_attribute('class').find('sidebar-expanded') != -1):
            HordPage.verifySidebarExpanded()
            if captureScreenshot:
                takeScreenshot(f"assets/screenshots/hord_sidebar_expanded.png")
        else:
            collapsedSidebarElements = UI_Actions.getElements(hord_locators.collapsed_sidebar_items)
            for element in collapsedSidebarElements:
                Verifications.verifyElementAttributeDoesNotContain(element, 'class', hord_locators.expanded_sidebar_items)
                
            if captureScreenshot:
                takeScreenshot(f"assets/screenshots/hord_sidebar_collapsed.png")

    def toggleSidebar():
        sidebar_toggler = HordPage.getSidebarToggle()
        UI_Actions.hoverAndClick(sidebar_toggler)
            
    def getSidebar():
        sidebar: WebElement = UI_Actions.getElement(hord_locators.sidebar)
        return sidebar

    def getSidebarToggle():
        sidebar_toggler: WebElement = UI_Actions.getElement(hord_locators.sidebar_toggler)
        return sidebar_toggler

    def verifySidebarExpanded():
        expanded_sidebar_items: WebElement = UI_Actions.getElements(hord_locators.expanded_sidebar_items)
        Verifications.verifyIntAbove(len(expanded_sidebar_items), 0)