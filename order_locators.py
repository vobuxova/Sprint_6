from selenium.webdriver.common.by import By

class OrderLocators:
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g") 
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//a[@href='/']")
    YANDEX_LOGO = (By.XPATH, "//a[@href='//yandex.ru']")
    COOKIE_BUTTON = (By.CLASS_NAME, "App_CookieButton__3cvqF")
    
    
class OrderFieldLocators:
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_DATA = lambda metro: (By.XPATH, f"//button/div[text()='{metro}']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DROP_DOWN_BUTTON = (By.CLASS_NAME, "Dropdown-arrow")
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//select[@placeholder='Срок аренды']")
    RENT_DATA = lambda rent: (By.XPATH, f"//div[text()='{rent}']")
    CONFIRM_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons__')]/button[normalize-space()='Заказать']")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
    ORDER_STATUS = (By.XPATH, "//button[text()='Посмотреть статус']")
    BLACK = (By.ID, "black")
    GREY = (By.ID, "grey")