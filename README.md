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



