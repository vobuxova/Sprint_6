from selenium.webdriver.common.by import By


class QuestionLocators:
    COST_QUESTION = (By.XPATH, "//*[@id='accordion__heading-0']")
    FEW_OBJECTS_QUESTION = (By.XPATH, "//*[@id='accordion__heading-1']")
    TIME_RENT_QUESTION = (By.XPATH, "//*[@id='accordion__heading-2']")
    TODAY_ORDER_QUESTION = (By.XPATH, "//*[@id='accordion__heading-3']")
    EXTENSION_OR_REFUND_QUESTION = (By.XPATH, "//*[@id='accordion__heading-4']")
    CHARGER_WITH_ORDER_QUESTION = (By.XPATH, "//*[@id='accordion__heading-5']")
    CANSEL_ORDER_QUESTION = (By.XPATH, "//*[@id='accordion__heading-6']")
    AREA_OF_ORDER_QUESTION = (By.XPATH, "//*[@id='accordion__heading-7']")
    
class AnswerLocators:
    COST_ANSWER = (By.XPATH, "//*[@id='accordion__panel-0']/p")
    FEW_OBJECTS_ANSWER = (By.XPATH, "//*[@id='accordion__panel-1']/p")
    TIME_RENT_ANSWER = (By.XPATH, "//*[@id='accordion__panel-2']/p")
    TODAY_ORDER_ANSWER = (By.XPATH, "//*[@id='accordion__panel-3']/p")
    EXTENSION_OR_REFUND_ANSWER = (By.XPATH, "//*[@id='accordion__panel-4']/p")
    CHARGER_WITH_ORDER_ANSWER = (By.XPATH, "//*[@id='accordion__panel-5']/p")
    CANSEL_ORDER_ANSWER = (By.XPATH, "//*[@id='accordion__panel-6']/p")
    AREA_OF_ORDER_ANSWER = (By.XPATH, "//*[@id='accordion__panel-7']/p")