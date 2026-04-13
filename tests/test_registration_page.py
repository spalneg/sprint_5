from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from urls import REGISTER_URL


class TestRegistrationPage:

    def test_registration_valid_data_success(self, name, new_email, new_password, browser):
        browser.get(REGISTER_URL)
        browser.find_element(*NAME).send_keys(name)
        browser.find_element(*NEW_LOGIN).send_keys(new_email)
        browser.find_element(*PASSWORD).send_keys(new_password)
        browser.find_element(*REGISTER_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((LOGIN_BUTTON)))
        browser.find_element(*LOGIN).send_keys(new_email)
        browser.find_element(*PASSWORD).send_keys(new_password)
        browser.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((ACCOUNT_BUTTON)))
        browser.find_element(*ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((CURRENT_LOGIN_FIELD)))
        element = browser.find_element(*CURRENT_LOGIN_FIELD).get_attribute('value')
        assert element == new_email    

    def test_registration_invalid_password_shows_error(self, name, new_email, invalid_password, browser):
        browser.get(REGISTER_URL)
        browser.find_element(*NAME).send_keys(name)
        browser.find_element(*NEW_LOGIN).send_keys(new_email)
        browser.find_element(*PASSWORD).send_keys(invalid_password)
        browser.find_element(*REGISTER_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((PASSWORD_ERROR)))
        elements = browser.find_elements(*PASSWORD_ERROR)
        assert len(elements) == 1
        