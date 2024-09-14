from locators import Locators
import data
from conftest import driver


# Тест на оформление товара
class TestShopBuy:
    def test_shop_buy(self,driver):
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
        click_on_product = driver.find_element(*Locators.BTN_PRODUCT)
        click_on_product.click()
        # Клик по кнопке ADD_TO_CARD
        click_on_add = driver.find_element(*Locators.BTN_ADD_TO_CARD)
        click_on_add.click()
        # Клик по кнопке значка Корзина
        click_basket = driver.find_element(*Locators.BTN_BASKET)
        click_basket.click()
        # Проверка что товар в корзине
        head_product = driver.find_element(*Locators.HEAD_PRODUCT)
        assert head_product.is_displayed() and head_product.text == 'Sauce Labs Bike Light'
        # Клик по кнопке CHECOUNT
        click_checount = driver.find_element(*Locators.BTN_CHECOUNT)
        click_checount.click()
        # Клик по полю FIRSTNAME
        click_firstname = driver.find_element(*Locators.FIELD_FIRSTNAME)
        click_firstname.click()
        # Заполнение поля FIRSTNAME
        click_firstname.send_keys(data.FIRSTNAME)
        # Клик по полю LAST_NAME
        click_lastname = driver.find_element(*Locators.FIELD_LAST_NAME)
        click_lastname.click()
        # Заполнение поля LAST_NAME
        click_lastname.send_keys(data.LASTNAME)
        # Клик по полю ZIP
        click_zip = driver.find_element(*Locators.FIELD_ZIP)
        click_zip.click()
        # Заполнение поля ZIP
        click_zip.send_keys(data.ZIP)
        # Клик по кнопке CONTINUE
        click_continue = driver.find_element(*Locators.BTN_CONTINUE)
        click_continue.click()
        # Проверка что товар оформился
        head_product = driver.find_element(*Locators.HEAD_PRODUCT)
        assert head_product.is_displayed() and head_product.text == 'Sauce Labs Bike Light'
        # Клик по кнопке FINISH
        click_finish = driver.find_element(*Locators.BTN_FINISH)
        click_finish.click()
        # Проверка что покупка завершена успешно
        head_order = driver.find_element(*Locators.HEAD_THANK_YOU)
        assert head_order.is_displayed() and head_order.text == 'Thank you for your order!'



