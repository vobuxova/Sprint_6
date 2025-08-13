from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        ActionChains(self.driver).move_to_element(element).perform()
        element.click()

    def scroll_to_bottom(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    def get_current_url(self):
        return self.driver.current_url
    
    def current_window_handle(self):
        return self.driver.current_window_handle

    def quit(self):
        self.driver.quit()