from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from urls import *


class TestLoginPage:

    def test_login_button_on_main_page_login_success(self, email, password, browser):
        browser.get(MAIN_URL)
        browser.find_element(*ACCOUNT_LOGIN_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((LOGIN_BUTTON)))
        browser.find_element(*LOGIN).send_keys(email)
        browser.find_element(*PASSWORD).send_keys(password)
        browser.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((ACCOUNT_BUTTON)))
        browser.find_element(*ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((CURRENT_LOGIN_FIELD)))
        element = browser.find_element(*CURRENT_LOGIN_FIELD).get_attribute('value')
        assert element == email    
        
    def test_personal_account_button_login_success(self, email, password, browser):
        browser.get(MAIN_URL)
        browser.find_element(*ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((LOGIN_BUTTON)))
        browser.find_element(*LOGIN).send_keys(email)
        browser.find_element(*PASSWORD).send_keys(password)
        browser.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((ACCOUNT_BUTTON)))
        browser.find_element(*ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((CURRENT_LOGIN_FIELD)))
        element = browser.find_element(*CURRENT_LOGIN_FIELD).get_attribute('value')
        assert element == email 

    def test_login_button_in_registration_form_login_success(self, email, password, browser):
        browser.get(REGISTER_URL)
        browser.find_element(*SIGN_IN_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((LOGIN_BUTTON)))
        browser.find_element(*LOGIN).send_keys(email)
        browser.find_element(*PASSWORD).send_keys(password)
        browser.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((ACCOUNT_BUTTON)))
        browser.find_element(*ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((CURRENT_LOGIN_FIELD)))
        element = browser.find_element(*CURRENT_LOGIN_FIELD).get_attribute('value')
        assert element == email 

    def test_login_button_in_password_recovery_form_login_success(self, email, password, browser):
        browser.get(PASSWORD_RECOVERY_URL)
        browser.find_element(*SIGN_IN_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((LOGIN_BUTTON)))
        browser.find_element(*LOGIN).send_keys(email)
        browser.find_element(*PASSWORD).send_keys(password)
        browser.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((ACCOUNT_BUTTON)))
        browser.find_element(*ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((CURRENT_LOGIN_FIELD)))
        element = browser.find_element(*CURRENT_LOGIN_FIELD).get_attribute('value')
        assert element == email 