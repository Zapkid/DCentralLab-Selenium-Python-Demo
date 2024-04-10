from commonOps import driver
from pages.hordPage import HordPage


def test_hord():
    
    # Should be in before hook
    driver.get("https://staging-app.hord.fi")

    HordPage.verifySidebarToggled()         
        
    HordPage.toggleSidebar()
    HordPage.verifySidebarToggled(True)
               
    HordPage.toggleSidebar()
    HordPage.verifySidebarToggled(True)
    