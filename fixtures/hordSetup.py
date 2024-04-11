import allure
import pytest
from utils.base import driver

@pytest.fixture()
@allure.title("Setup for the Hord app test")
def hord_setup():
    driver.get("https://staging-app.hord.fi")
    yield