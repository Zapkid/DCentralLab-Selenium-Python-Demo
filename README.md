![DCentralLab](assets/assignment/DCentralLab_logo.png)

# DCentralLab-Selenium-Python-Demo

This project demonstrates my ability to build an automation testing infrastructure POC with tests using Page Object design pattern, in Python.

![DCentralLab Products](assets/assignment/DCentralLab_products.png)

[Full assignment document found here.](assets/assignment/DCentraLab%20-%20QA%20&%20Support%20Engineer%20-%20Home%20Assignments.md)


## Technology stack
* Selenium
* Python
* PyTest
* Allure Reports


## Project structure
* UI actions & verifications are located in `extensions` folder.
* Fixtures used to initialize test functions.
* Locators to store selectors for UI elements.
* Pages representing web pages under test holding page specific functionality.
* Tests folder containing test logic.
* Utils - `base.py` to hold global variables & other utils for common operations across tests like `screenshot.py`.
* `conftest.py` - default configuration for pytest & global hooks.


## Manual Assignments
* Briefly explain Crypto concepts: blockchain, smart contract, bridge, GAS token, ERC-20 token, wallet and the [ChainPort bridge](https://www.chainport.io). [Done](manual/crypto_concepts.md).
* Transaction history page tests suite. [Not Done](manual/transaction_tab_test_cases.md).
* Bonus task - Porting fees protocol test cases. [Not Done].


## Automation Assignments
* TokensFarm app Element Locator - [Done](tests/test_tokens_farm.py).\
CSS Selector - `#farm-chain` or `[id='farm-chain']`\
XPATH Selector - `//*[@id='farm-chain']`
![allure_report_tokens_farm_test](assets/allure_reports/allure_report_tokens_farm_test.png "allure_report_tokens_farm_test")

* QA automation infrastructure project improvements - [Done](infra_improvements.md).

* Hord app verify Sidebar. [Done](tests/test_hord.py).
![allure_report_hord_sidebar_test](assets/allure_reports/allure_report_hord_sidebar_test.png "allure_report_hord_sidebar_test")


## Run automation tests
* run `python -m pytest --alluredir allure-results` in the terminal to run the tests & generate allure reports.
* run `allure serve allure-results` in the terminal to open the report in a web browser.

## Estimated time worked on the project (hrs): 
~ 12 hrs