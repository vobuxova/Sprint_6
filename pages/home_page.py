from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from .base_page import BasePage
from ..order_locators import OrderLocators
from ..data import Urls

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = Urls.base_url

    def open(self):
        self.driver.get(self.base_url)

    def click_faq_question(self, question_locator, answer_locator):
        element = self.find_element(question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_element(question_locator)
        return self.find_element(answer_locator).text 

    def click_order_button(self, is_top=True):
        if is_top:
            locator = OrderLocators.ORDER_BUTTON_TOP
            element = self.find_element(locator)
        else:
            locator = OrderLocators.ORDER_BUTTON_BOTTOM
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def click_scooter_logo(self):
        self.click_element(OrderLocators.SCOOTER_LOGO)
        return self.get_current_url()

    def click_yandex_logo(self):
        original_window = self.driver.current_window_handle
        self.click_element(OrderLocators.YANDEX_LOGO)

        self.wait.until(EC.number_of_windows_to_be(2))

        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)

        self.wait.until(lambda d: d.current_url != "about:blank")

        url = self.get_current_url()
        self.driver.close()
        self.driver.switch_to.window(original_window)
        return url

    def click_top_order_button(self):
        self.click_element(*OrderLocators.ORDER_BUTTON_TOP)

    def click_bottom_order_button(self):
        buttons = self.driver.find_elements(*OrderLocators.ORDER_BUTTON_BOTTOM)
        if len(buttons) >= 2:
            button = buttons[1]
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
            ActionChains(self.driver).move_to_element(button).perform()
            self.wait.until(EC.element_to_be_clickable(button)).click()
        else:
            raise Exception("Кнопка внизу не найдена")

    def close_cookie_banner(self):
        try:
            cookie_button = self.wait.until(EC.element_to_be_clickable(OrderLocators.COOKIE_BUTTON))
            cookie_button.click()
        except:
            print("Cookie banner not found or not clickable")