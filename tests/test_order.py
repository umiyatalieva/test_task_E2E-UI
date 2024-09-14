from locators import Locators
import data
from conftest import driver


# Тест на выбор товара и добавление в корзину
class TestOrder:
    def test_order(self,driver):
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
        # Клик по кнопке LOGIN
        click_btn_login = driver.find_element(*Locators.BTN_LOGIN)
        click_btn_login.click()
        # Клик по кнопке товара "Sauce Labs Bike Light"
        click_on_product=driver.find_element(*Locators.BTN_PRODUCT)
        click_on_product.click()
        # Клик по кнопке ADD_TO_CARD
        click_on_add = driver.find_element(*Locators.BTN_ADD_TO_CARD)
        click_on_add.click()
        # Проверка что товвар добавлен в корзину
        quatity_product=driver.find_element(*Locators.QUANTITY_PRODUCT)
        assert quatity_product.is_displayed() and quatity_product.text == '1'