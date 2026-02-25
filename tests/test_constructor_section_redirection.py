from locators import *
from urls import MAIN_URL


class TestConstructorSectionRedirection:

    def test_filling_section_redirected_on_scroll(self, browser):
        browser.get(MAIN_URL)
        element = browser.find_element(*FILLING_HEADER)
        browser.execute_script("arguments[0].scrollIntoView();", element)
        assert 'tab_tab_type_current__2BEPc' in browser.find_element(*FILLING_BUTTON).get_attribute('class')

    def test_sauce_section_redirected_on_scroll(self, browser):
        browser.get(MAIN_URL)
        element = browser.find_element(*SAUSE_HEADER)
        browser.execute_script("arguments[0].scrollIntoView();", element)
        assert 'tab_tab_type_current__2BEPc' in browser.find_element(*SAUSE_BUTTON).get_attribute('class')

    def test_bun_section_redirected_on_scroll(self, browser):
        browser.get(MAIN_URL)
        element = browser.find_element(*BUN_HEADER)
        browser.execute_script("arguments[0].scrollIntoView();", element)
        assert 'tab_tab_type_current__2BEPc' in browser.find_element(*BUN_BUTTON).get_attribute('class')