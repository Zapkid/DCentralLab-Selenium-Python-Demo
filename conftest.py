from commonOps import driver

def pytest_sessionstart(session):
    driver.maximize_window()

def pytest_sessionfinish(session, exitstatus):
    driver.quit()