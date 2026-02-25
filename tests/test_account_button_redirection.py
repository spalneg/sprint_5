from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from urls import *
class TestAccountButtonRedirection:
    
    def test_account_button_redirection_to_account_page_by_click(self, email, password, browser):
        browser.get(LOGIN_URL)
        browser.find_element(*LOGIN).send_keys(email)
        browser.find_element(*PASSWORD).send_keys(password)
        browser.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((ACCOUNT_BUTTON)))
        browser.find_element(*ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((LOGIN)))
        assert browser.current_url == ACCOUNT_URL
    