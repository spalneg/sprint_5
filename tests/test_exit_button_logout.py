from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from urls import LOGIN_URL


class TestExitButtonLogout:

    def test_exit_button_logout_by_click(self, email, password, browser):
        browser.get(LOGIN_URL)
        browser.find_element(*LOGIN).send_keys(email)
        browser.find_element(*PASSWORD).send_keys(password)
        browser.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((ACCOUNT_BUTTON)))
        browser.find_element(*ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((CURRENT_LOGIN_FIELD)))
        browser.find_element(*LOGOUT_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((LOGIN_BUTTON)))
        assert browser.current_url == LOGIN_URL
    