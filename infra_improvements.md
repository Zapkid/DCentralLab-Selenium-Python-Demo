Auto Qa Infra (branch: DEVELOP) possible improvements:

> *Escape from Object Orientation and enjoy the simpler practices of Object Based programming instead.* [python-patterns.guide](https://python-patterns.guide)

* **Avoid inheritance in the page object model** of BasePage.py.
* Code segments can be refactored to increase readability & understanding of what the code does & to avoid code duplication.
* Comments that explain what the code does are redundant. Comments should be used to explain why the code is there rather than what it does. **Reduce comments noise**.
* Logs like "window had maximize" only adds noise to the logs. **Refine logging messages to prioritize relevant information and eliminate unnecessary noise.** 
* Hooks - Consider **merging multiple global hooks** into one, thus creating one localized place for the hook. Enabling a faster & clearer overview of all the actions performed in a hook (like a before_all).
* Locators - **Move all locators from page objects to locator files** - this avoids duplication across multiple test files. Also, avoid using contains, should be more future-proofed by adding unique data-testid property on the elements.
* Scheduled test runs.
* Run tests on command & by groupings.
* Run tests in parallel if possible using multiprocessing or distributed testing frameworks like pytest-xdist, to reduce test execution time.
* **Allure Reports** - Detailed test results reports.
* Report summary sent to Slack on a dedicated channel.
* Implement integration to link automated tests with test cases in a test management platform.
* Add API testing for backend validation.
* Containerization: Dockerize the automation framework and dependencies to create lightweight, portable containers for easier setup, deployment, and scalability across different environments.
* Support Mobile testing
* Optional: Video recordings of failed tests

---

**BasePage.py should be broken up to two files. UI_Actions.py for functions that perform actions on web elements, and Verifications.py to hold all functions that make assertions on web elements.**

UI_Actions.py & Verifications.py should be moved to a different directory (like extensions).

**Complex flows involving more than one page should be saved as a workflow function in a workflows.py file.**

---

In Screenshot.py:

def get_current_datetime - function should be moved to `date_time.py` in utils folder to be reused globally, add parameter for datetime format if needed.

---

Redundant comment example: 

Get driver name\
driver_type = request.cls.driver.name\
refactor to -> driver_type = get_driver_name(request).\
Also, this can be saved as global variable in the before_all hook, instead of being called on each failed test, as this value does not change during a run.

---

HTTPStatusCodes.py - can use `from http import HTTPStatus` or `import http.client` instead of manually entering status codes.

---

Instead of passing the element name & locator separately, consider passing just 1 object containing these attributes & destruct it:

###### Current code -
def is_confirm_button_exist(self):\
    return self.is_element_exist("CONFIRM_BUTTON", CONFIRM_BUTTON)

###### Suggested improvement -
confirm_button = { "name": "CONFIRM_BUTTON", locator: CONFIRM_BUTTON }

def is_confirm_button_exist(self):\
    return self.is_element_exist(confirm_button)

def is_element_exist(self, element):\
    element_name = element.get("name")\
    element_locator = element.get("locator")\
    ...