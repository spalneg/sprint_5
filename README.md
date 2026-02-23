# Проект автоматизации тестирования сервиса Stellar Burgers 
Основа для написания автотестов — фреймворк pytest \
Команда для запуска — pytest -v 

**Описание тестов** 

Регистрация - test_registration_page.py \
**test_registration_valid_data_success** # Проверка успешной регистрации нового пользователя с генерацией логина и пароля  
**test_registration_invalid_password_shows_error** # Проверка возникновения ошибки при невалидном пароле 

Вход  - test_login_page.py \
**test_login_button_on_main_page_login_success** # Проверка входа по кнопке «Войти в аккаунт» на главной \
**test_personal_account_button_login_success** # Проверка входа через кнопку «Личный кабинет» \
**test_login_button_in_registration_form_login_success** # Проверка входа через кнопку в форме регистрации \
**test_login_button_in_password_recovery_form_login_success** # Проверка входа через кнопку в форме восстановления пароля 

Переход в личный кабинет - test_account_button_redirection.py \
**test_account_button_redirection_to_account_page_by_click** # Проверка перехода по клику на «Личный кабинет» 

Переход из личного кабинета в конструктор - test_account_to_constructor_redirection.py \
**test_constructor_button_redirection_on_main_page_by_click** # Проверка перехода по клику на «Конструктор» \
**test_logo_click_redirection_on_main_page_by_click** # Проверка перехода по клику на логотип Stellar Burgers 

Выход из аккаунта - test_exit_button_logout.py \
**test_exit_button_logout_by_click** # Проверка выхода по кнопке «Выйти» в личном кабинете 

Раздел «Конструктор» - test_constructor_section_redirection.py \
**test_filling_section_redirected_on_scroll** # Проверка работы переходов к разделу «Начинки» по скроллу \
**test_sauce_section_redirected_on_scroll** # Проверка работы переходов к разделу «Соусы» по скроллу  
**test_bun_section_redirected_on_scroll** # Проверка работы переходов к разделу «Булки» по скроллу  


Используемые локаторы:  \
(By.XPATH, '//label[text()="Имя"]/parent::div/input') # Поле ввода имени в форме регистрации \
(By.XPATH, '//label[text()="Email"]/parent::div/input') # Поле ввода почты в форме регистрации и авторизации \
(By.XPATH, '//label[text()="Пароль"]/parent::div/input') # Поле ввода пароля в форме регистрации и авторизации \
(By.XPATH, '//button[text()="Зарегистрироваться"]') # Кнопка «Зарегистрироваться» в форме регистрации \
(By.XPATH, '//button[text()="Войти"]') # Кнопка «Войти» в форме авторизации \
(By.XPATH, '//p[@class="input__error text_type_main-default"][text()="Некорректный пароль"]') # Ошибка при вводе неправильного пароля \
(By.XPATH, '//p[text()="Личный Кабинет"]') # Кнопка перехода в личный кабинет \
(By.XPATH, '//label[text()="Логин"]/parent::div/input') # Поле ввода с логином авторизованного пользователя \
(By.CLASS_NAME, 'Auth_link__1fOlj') # Кнопка «Войти» на странице регистрации и восстановления пароля \
(By.XPATH,'//p[text()="Конструктор"]') Кнопка «Конструктор», ведущая на главную страницу \
(By.CLASS_NAME,'AppHeader_header__logo__2D0X2') # Логотип \
(By.XPATH, '//span[text()= "Булки"]/parent::div') # Кнопка выбора раздела «Булки» на главной странице \
(By.XPATH, '//span[text()= "Соусы"]/parent::div') # Кнопка выбора раздела «Соусы» на главной странице \
(By.XPATH, '//span[text()= "Начинки"]/parent::div') # Кнопка выбора раздела «Начинки» на главной странице \
(By.XPATH, '//h2[text()="Булки"]') # Заголовок раздела «Булки» на главной странице \
(By.XPATH, '//h2[text()="Соусы"]') # Заголовок раздела «Соусы» на главной странице \
(By.XPATH, '//h2[text()="Начинки"]') # Заголовок раздела «Начинки» на главной странице 
