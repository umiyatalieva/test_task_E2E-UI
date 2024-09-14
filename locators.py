from selenium.webdriver.common.by import By

class Locators:
    # Поле Username
    FIELD_USERNAME = (By.XPATH, "//*[@placeholder='Username']")
    # Поле Password
    FIELD_PASSWORD = (By.XPATH, "//*[@placeholder='Password']")
    # Кнопка Login
    BTN_LOGIN = (By.XPATH, "//*[@id='login-button']")
    # Кнопка товара "Sauce Labs Bike Light"
    BTN_PRODUCT = (By.XPATH, "//*[text()='Sauce Labs Bike Light']")
    # Кнопка Add to card
    BTN_ADD_TO_CARD = (By.XPATH, "//*[@id='add-to-cart']")
    # Кнопка Checount
    BTN_CHECOUNT = (By.XPATH, "//*[@id='checkout']")
    # Поле Firstname
    FIELD_FIRSTNAME = (By.XPATH, "//*[@id='first-name']")
    # Поле Last name
    FIELD_LAST_NAME = (By.XPATH, "//*[@id='last-name']")
    # Поле Zip/Postal code
    FIELD_ZIP = (By.XPATH, "//*[@id='postal-code']")
    # Кнопка Continue
    BTN_CONTINUE = (By.XPATH, "//*[@id='continue']")
    # Кнопка Finish
    BTN_FINISH = (By.XPATH, "//*[@id='finish']")
    # Заголовок Thank you for your order!
    HEAD_THANK_YOU = (By.XPATH, "//h2[text()='Thank you for your order!']")
    # Кнопка Корзина
    BTN_BASKET = (By.XPATH, "//*[@class='shopping_cart_link']")
    # Заголовок товара в корзине
    HEAD_PRODUCT=(By.XPATH, "//*[text()='Sauce Labs Bike Light']")
    # Количество товара на кнопке Корзина
    QUANTITY_PRODUCT=(By.XPATH,"//*[text()='1']")
    # Заголовок страницы "Products"
    HEAD_MAIN_PRODUCTS=(By.XPATH,"//*[text()='Products']")


