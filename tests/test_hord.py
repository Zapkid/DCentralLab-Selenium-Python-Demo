from commonOps import driver
from pages.hordPage import HordPage


def test_hord():
    
    # Should be in before hook
    driver.get("https://staging-app.hord.fi")

    HordPage.verifySidebarToggledState()         
        
    HordPage.toggleSidebar()
    HordPage.verifySidebarToggledState(True)
               
    HordPage.toggleSidebar()
    HordPage.verifySidebarToggledState(True)
    