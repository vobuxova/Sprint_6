import allure
from selenium import webdriver
from pages.home_page import HomePage
from main_questions_locators import QuestionLocators, AnswerLocators

@allure.feature("FAQ")
class TestFAQ:

    @allure.story("Сколько это стоит?")    
    def test_faq_questions_cost_question(self):
        home_page = HomePage(webdriver.Firefox())
        home_page.driver.get('https://qa-scooter.praktikum-services.ru/')
        expected_answer = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        answer = home_page.click_faq_question(QuestionLocators.COST_QUESTION, AnswerLocators.COST_ANSWER)
        assert answer == expected_answer, f"Ответ для вопроса не совпадает: ожидался {expected_answer}, получен {answer}"
        home_page.driver.quit() 

    @allure.story("Можно ли заказать несколько самокатов?")    
    def test_faq_questions_few_object_question(self):
        home_page = HomePage(webdriver.Firefox())
        home_page.driver.get('https://qa-scooter.praktikum-services.ru/')
        expected_answer = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        answer = home_page.click_faq_question(QuestionLocators.FEW_OBJECTS_QUESTION, AnswerLocators.FEW_OBJECTS_ANSWER)
        assert answer == expected_answer, f"Ответ для вопроса не совпадает: ожидался {expected_answer}, получен {answer}"
        home_page.driver.quit() 

    @allure.story("Когда начинается аренда?")    
    def test_faq_questions_time_rent_question(self):
        home_page = HomePage(webdriver.Firefox())
        home_page.driver.get('https://qa-scooter.praktikum-services.ru/')
        expected_answer = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        answer = home_page.click_faq_question(QuestionLocators.TIME_RENT_QUESTION, AnswerLocators.TIME_RENT_ANSWER)
        assert answer == expected_answer, f"Ответ для вопроса не совпадает: ожидался {expected_answer}, получен {answer}"
        home_page.driver.quit() 

    @allure.story("Можно ли заказать сегодня?")    
    def test_faq_questions_today_order_question(self):
        home_page = HomePage(webdriver.Firefox())
        home_page.driver.get('https://qa-scooter.praktikum-services.ru/')
        expected_answer = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        answer = home_page.click_faq_question(QuestionLocators.TODAY_ORDER_QUESTION, AnswerLocators.TODAY_ORDER_ANSWER)
        assert answer == expected_answer, f"Ответ для вопроса не совпадает: ожидался {expected_answer}, получен {answer}"
        home_page.driver.quit()   

    @allure.story("Можно ли продлить или отменить заказ?")    
    def test_faq_questions_extension_or_refund_question(self):
        home_page = HomePage(webdriver.Firefox())
        home_page.driver.get('https://qa-scooter.praktikum-services.ru/')
        expected_answer = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        answer = home_page.click_faq_question(QuestionLocators.EXTENSION_OR_REFUND_QUESTION, AnswerLocators.EXTENSION_OR_REFUND_ANSWER)
        assert answer == expected_answer, f"Ответ для вопроса не совпадает: ожидался {expected_answer}, получен {answer}"
        home_page.driver.quit()  

    @allure.story("Нужна ли зарядка?")    
    def test_faq_questions_charger_with_order_question(self):
        home_page = HomePage(webdriver.Firefox())
        home_page.driver.get('https://qa-scooter.praktikum-services.ru/')
        expected_answer = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        answer = home_page.click_faq_question(QuestionLocators.CHARGER_WITH_ORDER_QUESTION, AnswerLocators.CHARGER_WITH_ORDER_ANSWER)
        assert answer == expected_answer, f"Ответ для вопроса не совпадает: ожидался {expected_answer}, получен {answer}"
        home_page.driver.quit()  

    @allure.story("Можно ли отменить заказ?")    
    def test_faq_questions_cansel_order_question(self):
        home_page = HomePage(webdriver.Firefox())
        home_page.driver.get('https://qa-scooter.praktikum-services.ru/')
        expected_answer = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        answer = home_page.click_faq_question(QuestionLocators.CANSEL_ORDER_QUESTION, AnswerLocators.CANSEL_ORDER_ANSWER)
        assert answer == expected_answer, f"Ответ для вопроса не совпадает: ожидался {expected_answer}, получен {answer}"
        home_page.driver.quit()   

    @allure.story("Где работает доставка?")    
    def test_faq_questions_area_of_order_question(self):
        home_page = HomePage(webdriver.Firefox())
        home_page.driver.get('https://qa-scooter.praktikum-services.ru/')
        expected_answer = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        answer = home_page.click_faq_question(QuestionLocators.AREA_OF_ORDER_QUESTION, AnswerLocators.AREA_OF_ORDER_ANSWER)
        assert answer == expected_answer, f"Ответ для вопроса не совпадает: ожидался {expected_answer}, получен {answer}"
        home_page.driver.quit()   
        
    