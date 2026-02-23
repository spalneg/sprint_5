from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_registration_valid_data_success(name, new_email, new_password):
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.education-services.ru/register')
    browser.find_element(By.XPATH, '//label[text()="Имя"]/parent::div/input').send_keys(name)
    browser.find_element(By.XPATH, '//label[text()="Email"]/parent::div/input').send_keys(new_email)
    browser.find_element(By.XPATH,  '//label[text()="Пароль"]/parent::div/input').send_keys(new_password)
    browser.find_element(By.XPATH, '//button[text()="Зарегистрироваться"]').click()
    WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[text()="Войти"]')))
    browser.find_element(By.XPATH, '//label[text()="Email"]/parent::div/input').send_keys(new_email)
    browser.find_element(By.XPATH, '//label[text()="Пароль"]/parent::div/input').send_keys(new_password)
    browser.find_element(By.XPATH, '//button[text()="Войти"]').click()
    WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//p[text()="Личный Кабинет"]')))
    browser.find_element(By.XPATH, '//p[text()="Личный Кабинет"]').click()
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//label[text()="Логин"]/parent::div/input')))
    element = browser.find_element(By.XPATH, '//label[text()="Логин"]/parent::div/input').get_attribute('value')
    assert element == new_email    
    browser.quit()

def test_registration_invalid_password_shows_error(name, new_email, invalid_password):
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.education-services.ru/register')
    browser.find_element(By.XPATH, '//label[text()="Имя"]/parent::div/input').send_keys(name)
    browser.find_element(By.XPATH, '//label[text()="Email"]/parent::div/input').send_keys(new_email)
    browser.find_element(By.XPATH, '//label[text()="Пароль"]/parent::div/input').send_keys(invalid_password)
    browser.find_element(By.XPATH, '//button[text()="Зарегистрироваться"]').click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//p[@class="input__error text_type_main-default"][text()="Некорректный пароль"]')))
    elements = browser.find_elements(By.XPATH, '//p[@class="input__error text_type_main-default"][text()="Некорректный пароль"]')
    assert len(elements) == 1
    browser.quit()    