import pytest
import allure

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.order_page import OrderPage


@allure.title("Инициализация драйвера Firefox")
@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

@allure.feature("Оформление заказа")
@allure.story("Позитивный сценарий с параметризацией")
@pytest.mark.parametrize("is_top_button, order_data", [
    (True, {
        "first_name": "Иван",
        "last_name": "Иванов",
        "address": "ул. Пушкина, д.1",
        "metro": "Черкизовская",
        "phone": "+79998887766",
        "date": "12.08.2025",
        "rent_duration": "двое суток",
        "color": "black"
    }),
    (False, {
        "first_name": "Анна",
        "last_name": "Петрова",
        "address": "ул. Ленина, д.5",
        "metro": "Сокольники",
        "phone": "+79991112233",
        "date": "15.08.2025",
        "rent_duration": "сутки",
        "color": "grey"
    }),
])
def test_successful_order(driver, is_top_button, order_data):
    home_page = HomePage(driver)
    home_page.open()
    home_page.close_cookie_banner()
    home_page.click_order_button(is_top=is_top_button)

    order_page = OrderPage(driver)
    order_page.fill_order_form(order_data)
    assert order_page.is_order_successful(), "Окно подтверждения заказа не появилось"
    success_text = order_page.wait.until(
    EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Заказ оформлен')]"))
)
    assert "Заказ оформлен" in success_text.text

@allure.feature("Навигация")
@allure.story("Переход по логотипу Самоката на главную страницу")
def test_scooter_logo_redirects_to_home(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.close_cookie_banner()
    home_page.click_order_button(is_top=True)

    order_page = OrderPage(driver)
    home_url = home_page.base_url
    redirected_url = home_page.click_scooter_logo()
    assert redirected_url == home_url, f"Ожидался редирект на {home_url}, но был {redirected_url}"

@allure.feature("Навигация")
@allure.story("Переход по логотипу Яндекса на Дзен")
def test_yandex_logo_opens_dzen(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.close_cookie_banner()
    home_page.click_order_button(is_top=True)

    order_page = OrderPage(driver)
    url = home_page.click_yandex_logo()
    assert "dzen.ru" in url, f"Ожидался переход на Дзен, но url: {url}"
