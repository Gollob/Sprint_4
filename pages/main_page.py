import allure


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from locators.locator_main_page import MainLocators


class BasePage:
    @allure.step('Открываем браузер FireFox')
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://qa-scooter.praktikum-services.ru/'

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Not find locator{locator}')

    @allure.step('Открываем страницу https://qa-scooter.praktikum-services.ru/')
    def go_to_site(self):
        return self.driver.get(self.base_url)


class TestQuestion(BasePage):

    @allure.step('Нажатие на кнопку подтверждения Куки')
    def click_rcc_button(self):
        return self.find_element(MainLocators.LOCATOR_RCC_BUTTON, time=1).click()

    @allure.step('Нажатие на кнопку')
    def locator_clicks(self, locator_click):
        return self.find_element(locator_click, time=6).click()

    def text(self, text_faq):
        elemnt = self.find_element(text_faq)
        elemnt_text = elemnt.text
        return elemnt_text


class OrederButton(TestQuestion):
    @allure.step('Нажатие на кнопку заказать в хадаре')
    def click_on_header_order_button(self):
        return self.find_element(MainLocators.LOCATOR_MAIN_HEADER_ORDER_BUTTON, time=2).click()

    @allure.step('Нажатие на кнопку заказать')
    def click_on_order_button(self):
        return self.find_element(MainLocators.LOCATOR_MAIN_ORDER_BUTTON, time=2).click()
