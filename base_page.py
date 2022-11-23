from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://qa-scooter.praktikum-services.ru/'

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Not find locator{locator}')

    def go_to_site(self):
        return self.driver.get(self.base_url)




class MainLocators:
    LOCATOR_MAIN_HEADER_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    LOCATOR_MAIN_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']")
    LOCATOR_RCC_BUTTON = (By.XPATH, "//button[@id='rcc-confirm-button']")

    LOCATOR_YA_LOGO = (By.XPATH, "//img[@src='/assets/ya.svg']")
    LOCATOR_SCOOTER_LOGO = (By.XPATH, "//img[@src='/assets/scooter.svg']")

    LOCATOR_MAIN_QUESTION_1 = (By.CSS_SELECTOR, "#accordion__heading-0")
    LOCATOR_MAIN_QUESTION_2 = (By.CSS_SELECTOR, "#accordion__heading-1")
    LOCATOR_MAIN_QUESTION_3 = (By.CSS_SELECTOR, "#accordion__heading-2")
    LOCATOR_MAIN_QUESTION_4 = (By.CSS_SELECTOR, "#accordion__heading-3")
    LOCATOR_MAIN_QUESTION_5 = (By.CSS_SELECTOR, "#accordion__heading-4")
    LOCATOR_MAIN_QUESTION_6 = (By.CSS_SELECTOR, "#accordion__heading-5")
    LOCATOR_MAIN_QUESTION_7 = (By.CSS_SELECTOR, "#accordion__heading-6")
    LOCATOR_MAIN_QUESTION_8 = (By.CSS_SELECTOR, "#accordion__heading-7")

    LOCATOR_TEXT_QUESTION_1 = (By.XPATH, "//p[contains(text(),'Сутки — 400 рублей. Оплата курьеру — наличными или')]")
    LOCATOR_TEXT_QUESTION_2 = (By.XPATH, "//p[contains(text(),'Пока что у нас так: один заказ — один самокат. Есл')]")
    LOCATOR_TEXT_QUESTION_3 = (By.XPATH, "//p[contains(text(),'Допустим, вы оформляете заказ на 8 мая. Мы привози')]")
    LOCATOR_TEXT_QUESTION_4 = (By.XPATH, "//p[contains(text(),'Только начиная с завтрашнего дня. Но скоро станем ')]")
    LOCATOR_TEXT_QUESTION_5 = (By.XPATH, "//p[contains(text(),'Пока что нет! Но если что-то срочное — всегда можн')]")
    LOCATOR_TEXT_QUESTION_6 = (By.XPATH, "//p[contains(text(),'Самокат приезжает к вам с полной зарядкой. Этого х')]")
    LOCATOR_TEXT_QUESTION_7 = (By.XPATH, "//p[contains(text(),'Да, пока самокат не привезли. Штрафа не будет, объ')]")
    LOCATOR_TEXT_QUESTION_8 = (By.XPATH, "//p[contains(text(),'Да, обязательно. Всем самокатов! И Москве, и Моско')]")


class TestQuestion(BasePage):
    def click_rcc_button(self):
        return self.find_element(MainLocators.LOCATOR_RCC_BUTTON, time=1).click()

    def check_faq(self, locator_faq):
        return self.find_element(locator_faq, time=6).click()

    def text(self, text_faq):
        elemnt = self.find_element(text_faq)
        elemnt_text = elemnt.text
        return elemnt_text


class OrederButton(TestQuestion):
    def click_on_header_order_button(self):
        return self.find_element(MainLocators.LOCATOR_MAIN_HEADER_ORDER_BUTTON, time=2).click()

    def click_on_order_button(self):
        return self.find_element(MainLocators.LOCATOR_MAIN_ORDER_BUTTON, time=2).click()


# class FAQQuestion:
#     TEXT_QUESTION_1 = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
#     TEXT_QUESTION_2 = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
#     TEXT_QUESTION_3 = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
#     TEXT_QUESTION_4 = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
#     TEXT_QUESTION_5 = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
#     TEXT_QUESTION_6 = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
#     TEXT_QUESTION_7 = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
#     TEXT_QUESTION_8 = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
