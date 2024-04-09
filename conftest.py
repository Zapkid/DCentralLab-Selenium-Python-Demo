from commonOps import driver


def pytest_sessionfinish(session, exitstatus):
    driver.quit()