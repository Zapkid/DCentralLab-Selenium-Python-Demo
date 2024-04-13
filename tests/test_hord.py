import allure
from fixtures.hordSetup import hord_setup
from pages.hordPage import HordPage
from utils.screenshot import captureScreenshot

@allure.title("Verify Hord sidebar expands & collapses")
@allure.description("Should toggle sidebar & verify sidebar toggled states")
@allure.link("https://staging-app.hord.fi", name="Hord app Website")
def test_hord(hord_setup):
    
    HordPage.verifySidebarToggledState()         
        
    HordPage.toggleSidebar()
    HordPage.verifySidebarToggledState(captureScreenshot)
      
    # Toggling the sidebar a 2nd time to verify transitioning to both expanded & collapsed states
    HordPage.toggleSidebar()
    HordPage.verifySidebarToggledState(captureScreenshot)
    