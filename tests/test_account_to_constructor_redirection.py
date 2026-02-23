from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_constructor_button_redirection_on_main_page_by_click(email, password):
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.education-services.ru/login')
    browser.find_element(By.XPATH, '//label[text()="Email"]/parent::div/input').send_keys(email)
    browser.find_element(By.XPATH, '//label[text()="Пароль"]/parent::div/input').send_keys(password)
    browser.find_element(By.XPATH, '//button[text()="Войти"]').click()
    WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//p[text()="Личный Кабинет"]')))
    browser.find_element(By.XPATH, '//p[text()="Личный Кабинет"]').click()
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//label[text()="Логин"]/parent::div/input')))
    assert browser.current_url == 'https://stellarburgers.education-services.ru/account/profile'
    browser.find_element(By.XPATH,'//p[text()="Конструктор"]').click()
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//span[text()= "Булки"]/parent::div')))
    assert browser.current_url == 'https://stellarburgers.education-services.ru/'
    browser.quit()

def test_logo_click_redirection_on_main_page_by_click(email, password):
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.education-services.ru/login')
    browser.find_element(By.XPATH, '//label[text()="Email"]/parent::div/input').send_keys(email)
    browser.find_element(By.XPATH, '//label[text()="Пароль"]/parent::div/input').send_keys(password)
    browser.find_element(By.XPATH, '//button[text()="Войти"]').click()
    WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//p[text()="Личный Кабинет"]')))
    browser.find_element(By.XPATH, '//p[text()="Личный Кабинет"]').click()
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//label[text()="Логин"]/parent::div/input')))
    assert browser.current_url == 'https://stellarburgers.education-services.ru/account/profile'
    browser.find_element(By.CLASS_NAME,'AppHeader_header__logo__2D0X2').click()
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//span[text()= "Булки"]/parent::div')))
    assert browser.current_url == 'https://stellarburgers.education-services.ru/'
    browser.quit()
