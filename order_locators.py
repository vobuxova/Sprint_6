from selenium.webdriver.common.by import By

class OrderLocators:
    ORDER_BUTTON_TOP = (By.ID, "order-button-top") 
    ORDER_BUTTON_BOTTOM = (By.ID, "order-button-bottom")
    SCOOTER_LOGO = (By.XPATH, "//a[@href='/']")
    YANDEX_LOGO = (By.XPATH, "//a[@href='https://dzen.ru']")
    
class OrderFieldLocators:
    NAME_FIELD = (By.XPATH, "//input[@placeholder='Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='Адрес']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='Телефон']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='Станция метро']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATE_FIELD = (By.XPATH, "//input[@placeholder='Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//select[@placeholder='Срок аренды']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")