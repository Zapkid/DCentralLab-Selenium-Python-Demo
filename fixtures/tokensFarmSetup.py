import allure
import pytest
from utils.base import driver

@pytest.fixture()
@allure.title("Setup for the TokensFarm app test")
def tokens_farm_setup():
    driver.get("https://staging.tokensfarm.com/create#/staking")
    yield