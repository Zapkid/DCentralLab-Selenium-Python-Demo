import allure
import pytest
from base import driver
import time

@pytest.fixture()
@allure.title("Setup for the TokensFarm app test")
def tokens_farm_setup():
    driver.get("https://staging.tokensfarm.com/create#/staking")
    
    # Explicitly waiting for page to load the DOM
    # Not good practice, should be replaced by waiting for full page load
    time.sleep(5)
    yield