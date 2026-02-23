from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_button_on_main_page_login_success(email, password):
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.education-services.ru/')
    browser.find_element(By.XPATH, '//button[text()="Войти в аккаунт"]').click()
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//button[text()="Войти"]')))
    browser.find_element(By.XPATH, '//label[text()="Email"]/parent::div/input').send_keys(email)
    browser.find_element(By.XPATH, '//label[text()="Пароль"]/parent::div/input').send_keys(password)
    browser.find_element(By.XPATH, '//button[text()="Войти"]').click()
    WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//p[text()="Личный Кабинет"]')))
    browser.find_element(By.XPATH, '//p[text()="Личный Кабинет"]').click()
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//label[text()="Логин"]/parent::div/input')))
    element = browser.find_element(By.XPATH, '//label[text()="Логин"]/parent::div/input').get_attribute('value')
    assert element == email    
    browser.quit()

def test_personal_account_button_login_success(email, password):
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.education-services.ru/')
    browser.find_element(By.XPATH, '//p[text()="Личный Кабинет"]').click()
    WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[text()="Войти"]')))
    browser.find_element(By.XPATH, '//label[text()="Email"]/parent::div/input').send_keys(email)
    browser.find_element(By.XPATH, '//label[text()="Пароль"]/parent::div/input').send_keys(password)
    browser.find_element(By.XPATH, '//button[text()="Войти"]').click()
    WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//p[text()="Личный Кабинет"]')))
    browser.find_element(By.XPATH, '//p[text()="Личный Кабинет"]').click()
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//label[text()="Логин"]/parent::div/input')))
    element = browser.find_element(By.XPATH, '//label[text()="Логин"]/parent::div/input').get_attribute('value')
    assert element == email
    browser.quit()

def test_login_button_in_registration_form_login_success(email, password):
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.education-services.ru/register')
    browser.find_element(By.CLASS_NAME, 'Auth_link__1fOlj').click()
    WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[text()="Войти"]')))
    browser.find_element(By.XPATH, '//label[text()="Email"]/parent::div/input').send_keys(email)
    browser.find_element(By.XPATH, '//label[text()="Пароль"]/parent::div/input').send_keys(password)
    browser.find_element(By.XPATH, '//button[text()="Войти"]').click()
    WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//p[text()="Личный Кабинет"]')))
    browser.find_element(By.XPATH, '//p[text()="Личный Кабинет"]').click()
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//label[text()="Логин"]/parent::div/input')))
    element = browser.find_element(By.XPATH, '//label[text()="Логин"]/parent::div/input').get_attribute('value')
    assert element == email
    browser.quit()

def test_login_button_in_password_recovery_form_login_success(email, password):
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.education-services.ru/forgot-password')
    browser.find_element(By.CLASS_NAME, 'Auth_link__1fOlj').click()
    WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[text()="Войти"]')))
    browser.find_element(By.XPATH, '//label[text()="Email"]/parent::div/input').send_keys(email)
    browser.find_element(By.XPATH, '//label[text()="Пароль"]/parent::div/input').send_keys(password)
    browser.find_element(By.XPATH, '//button[text()="Войти"]').click()
    WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//p[text()="Личный Кабинет"]')))
    browser.find_element(By.XPATH, '//p[text()="Личный Кабинет"]').click()
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//label[text()="Логин"]/parent::div/input')))
    element = browser.find_element(By.XPATH, '//label[text()="Логин"]/parent::div/input').get_attribute('value')
    assert element == email
    browser.quit()