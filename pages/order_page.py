import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..order_locators import OrderFieldLocators
from .base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполняем форму заказа")
    def fill_order_form(self, data):
        self.find_element(OrderFieldLocators.NAME_FIELD).send_keys(data["first_name"])
        self.find_element(OrderFieldLocators.SURNAME_FIELD).send_keys(data["last_name"])
        self.find_element(OrderFieldLocators. ADDRESS_FIELD).send_keys(data["address"])

        self.find_element(OrderFieldLocators.METRO_FIELD).click()
        self.wait.until(EC.element_to_be_clickable(OrderFieldLocators.METRO_DATA(data['metro']))).click()

        self.find_element(OrderFieldLocators.PHONE_FIELD).send_keys(data["phone"])
        self.find_element(OrderFieldLocators.SUBMIT_BUTTON).click()

        date_input = self.wait.until(EC.visibility_of_element_located(OrderFieldLocators.DATE_FIELD))
        date_input.clear()
        date_input.send_keys(data["date"])
        date_input.send_keys(Keys.ENTER)

        self.find_element(OrderFieldLocators.DROP_DOWN_BUTTON).click()
        self.wait.until(EC.element_to_be_clickable(OrderFieldLocators.RENT_DATA(data['rent_duration']))).click()

        if data["color"] == "black":
            self.find_element(OrderFieldLocators.BLACK).click()
        elif data["color"] == "grey":
            self.find_element(OrderFieldLocators.GREY).click()

        order_button = self.wait.until(EC.element_to_be_clickable(OrderFieldLocators.CONFIRM_BUTTON))
        self.scroll_to_bottom(OrderFieldLocators.CONFIRM_BUTTON)
        order_button.click()

        confirm_button = self.wait.until(
            EC.element_to_be_clickable(OrderFieldLocators.YES_BUTTON)
        )
        confirm_button.click()

    def is_order_successful(self):
        try:
            self.wait.until(EC.visibility_of_element_located(OrderFieldLocators.ORDER_STATUS))
            return True
        except:
            return False

