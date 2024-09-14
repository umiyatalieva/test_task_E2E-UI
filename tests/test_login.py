from locators import Locators
import data
from conftest import driver


# Тест на авторизацию
class TestLogin:
    def test_login(self, driver):
        # Клик по полю USERNAME
        login_username = driver.find_element(*Locators.FIELD_USERNAME)
        login_username.click()
        # Заполнение поля USERNAME
        login_username.send_keys(data.USERNAME)
        # Клик по полю PASSWORD
        login_password = driver.find_element(*Locators.FIELD_PASSWORD)
        login_password.click()
        # Заполнение поля PASSWORD
        login_password.send_keys(data.PASSWORD)
        # Клик по кнопке  LOGIN
        click_btn_login = driver.find_element(*Locators.BTN_LOGIN)
        click_btn_login.click()
        # Проверка входа в аккаунт
        head_main_products=driver.find_element(*Locators.HEAD_MAIN_PRODUCTS)
        assert head_main_products.is_displayed() and head_main_products.text == 'Products'








