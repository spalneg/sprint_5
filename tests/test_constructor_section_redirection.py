from selenium import webdriver
from selenium.webdriver.common.by import By


def test_filling_section_redirected_on_scroll():
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.education-services.ru/')
    element = browser.find_element(By.XPATH, '//h2[text()="Начинки"]')
    browser.execute_script("arguments[0].scrollIntoView();", element)
    assert 'tab_tab_type_current__2BEPc' in browser.find_element(By.XPATH, '//span[text()= "Начинки"]/parent::div').get_attribute('class')
    browser.quit()

def test_sauce_section_redirected_on_scroll():
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.education-services.ru/')
    element = browser.find_element(By.XPATH, '//h2[text()="Соусы"]')
    browser.execute_script("arguments[0].scrollIntoView();", element)
    assert 'tab_tab_type_current__2BEPc' in browser.find_element(By.XPATH, '//span[text()= "Соусы"]/parent::div').get_attribute('class')
    browser.quit()

def test_bun_section_redirected_on_scroll():
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.education-services.ru/')
    element = browser.find_element(By.XPATH, '//h2[text()="Булки"]')
    browser.execute_script("arguments[0].scrollIntoView();", element)
    assert 'tab_tab_type_current__2BEPc' in browser.find_element(By.XPATH, '//span[text()= "Булки"]/parent::div').get_attribute('class')
    browser.quit()