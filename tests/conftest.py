import random
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture
def name():
    name = 'Burgerman'
    return name

@pytest.fixture
def new_email():
    new_email = f'mary_kup_44_{random.randint(100,999)}@yandex.ru'
    return new_email

@pytest.fixture
def new_password():
    new_password = random.randint(100000,999999)
    return new_password

@pytest.fixture
def invalid_password():
    invalid_password = random.randint(0,99999)
    return invalid_password

@pytest.fixture
def email():
    email = 'spalneg44@mail.ru'
    return email

@pytest.fixture
def password():
    password = '1234567890'
    return password