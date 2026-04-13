from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from urls import *


class TestAccountToConstructorRedirection:

    def test_constructor_button_redirection_on_main_page_by_click(self, email, password, browser):
        browser.get(LOGIN_URL)
        browser.find_element(*LOGIN).send_keys(email)
        browser.find_element(*PASSWORD).send_keys(password)
        browser.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((ACCOUNT_BUTTON)))
        browser.find_element(*ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((LOGIN)))
        assert browser.current_url == ACCOUNT_URL
        browser.find_element(*CONSTRUCTOR_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((BUN_BUTTON)))
        assert browser.current_url == MAIN_URL

    def test_logo_click_redirection_on_main_page_by_click(self, email, password, browser):
        browser.get(LOGIN_URL)
        browser.find_element(*LOGIN).send_keys(email)
        browser.find_element(*PASSWORD).send_keys(password)
        browser.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((ACCOUNT_BUTTON)))
        browser.find_element(*ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((LOGIN)))
        assert browser.current_url == ACCOUNT_URL
        browser.find_element(*LOGO).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((BUN_BUTTON)))
        assert browser.current_url == MAIN_URL
    
