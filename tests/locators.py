from selenium.webdriver.common.by import By

NAME = By.XPATH,'//fieldset[1]//input' # Поле ввода имени в форме регистрации \
NEW_LOGIN = By.XPATH,'//fieldset[2]//input' # Поле ввода почты в форме регистрации \
PASSWORD = By.XPATH,'//input[@name = "Пароль"]' # Поле ввода пароля в форме регистрации и авторизации\
LOGIN = By.XPATH,'//input[@name = "name"]' # Поле ввода почты в форме авторизации \
REGISTER_BUTTON = By.XPATH, '//button[text()="Зарегистрироваться"]' # Кнопка «Зарегистрироваться» в форме регистрации \
LOGIN_BUTTON = By.XPATH, '//button[text()="Войти"]' # Кнопка «Войти» в форме авторизации \
PASSWORD_ERROR = By.XPATH, '//p[@class="input__error text_type_main-default"][text()="Некорректный пароль"]' # Ошибка при вводе неправильного пароля \
ACCOUNT_BUTTON = By.XPATH, '//p[text()="Личный Кабинет"]' # Кнопка перехода в личный кабинет \
CURRENT_LOGIN_FIELD = By.XPATH, '//li[2]//input' # Поле ввода с логином авторизованного пользователя \
SIGN_IN_BUTTON = By.CLASS_NAME, 'Auth_link__1fOlj' # Кнопка «Войти» на странице регистрации и восстановления пароля \
CONSTRUCTOR_BUTTON = By.XPATH,'//p[text()="Конструктор"]' #Кнопка «Конструктор», ведущая на главную страницу \
LOGO = By.CLASS_NAME,'AppHeader_header__logo__2D0X2' # Логотип \
BUN_BUTTON = By.XPATH, '//div[@style = "display: flex;"]/div[1]' # Кнопка выбора раздела «Булки» на главной странице \
SAUSE_BUTTON = By.XPATH, '//div[@style = "display: flex;"]/div[2]'  # Кнопка выбора раздела «Соусы» на главной странице \
FILLING_BUTTON = By.XPATH, '//div[@style = "display: flex;"]/div[3]' # Кнопка выбора раздела «Начинки» на главной странице \
BUN_HEADER = By.XPATH, '//h2[text()="Булки"]' # Заголовок раздела «Булки» на главной странице \
SAUSE_HEADER = By.XPATH, '//h2[text()="Соусы"]' # Заголовок раздела «Соусы» на главной странице \
FILLING_HEADER = By.XPATH, '//h2[text()="Начинки"]' # Заголовок раздела «Начинки» на главной странице 
LOGOUT_BUTTON = By.XPATH, '//button[text()="Выход"]' #Кнопка выхода из аккаунта
ACCOUNT_LOGIN_BUTTON = By.XPATH, '//button[text()="Войти в аккаунт"]' # Кнопка «Войти в аккаунт» на главной странице