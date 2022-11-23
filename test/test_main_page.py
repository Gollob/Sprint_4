import allure
import time
from selenium.webdriver.common.by import By

from base_page import MainLocators
from base_page import TestQuestion


class TestLogo():
    @allure.suite('Test logo')
    @allure.feature('Test go to yndex')
    def test_ya_logo(self, browser):
        ya = TestQuestion(browser)
        ya.go_to_site()
        ya.click_rcc_button()
        ya.check_faq(MainLocators.LOCATOR_YA_LOGO)
        time.sleep(5)
        browser.switch_to.window(browser.window_handles[1])
        assert browser.current_url == 'https://dzen.ru/?yredirect=true'

    @allure.suite('Test logo')
    @allure.feature('Test go to SCOOTER')
    def test_scooter_logo(self, browser):
        scooter = TestQuestion(browser)
        scooter.go_to_site()
        scooter.click_rcc_button()
        scooter.check_faq(MainLocators.LOCATOR_SCOOTER_LOGO)
        time.sleep(5)
        assert browser.current_url == 'https://qa-scooter.praktikum-services.ru/'


class TestHowItWorks():
    @allure.suite('Test Вопросы о важном')
    @allure.feature('Test Сколько это стоит? И как оплатить?')
    def test_faq_1(self, browser):
        faq = TestQuestion(browser)
        faq.go_to_site()
        faq.click_rcc_button()
        faq.check_faq(MainLocators.LOCATOR_MAIN_QUESTION_1)
        faq.find_element(MainLocators.LOCATOR_TEXT_QUESTION_1)

    @allure.suite('Test Вопросы о важном')
    @allure.feature('Test Хочу сразу несколько самокатов! Так можно?')
    def test_faq_2(self, browser):
        faq = TestQuestion(browser)
        faq.go_to_site()
        faq.click_rcc_button()
        faq.check_faq(MainLocators.LOCATOR_MAIN_QUESTION_2)
        faq.find_element(MainLocators.LOCATOR_TEXT_QUESTION_2)

    @allure.suite('Test Вопросы о важном')
    @allure.feature('Test Как рассчитывается время аренды?')
    def test_faq_3(self, browser):
        faq = TestQuestion(browser)
        faq.go_to_site()
        faq.click_rcc_button()
        faq.check_faq(MainLocators.LOCATOR_MAIN_QUESTION_3)
        faq.find_element(MainLocators.LOCATOR_TEXT_QUESTION_3)

    @allure.suite('Test Вопросы о важном')
    @allure.feature('Test Можно ли заказать самокат прямо на сегодня?')
    def test_faq_4(self, browser):
        faq = TestQuestion(browser)
        faq.go_to_site()
        faq.click_rcc_button()
        faq.check_faq(MainLocators.LOCATOR_MAIN_QUESTION_4)
        faq.find_element(MainLocators.LOCATOR_TEXT_QUESTION_4)

    @allure.suite('Test Вопросы о важном')
    @allure.feature('Test Можно ли продлить заказ или вернуть самокат раньше?')
    def test_faq_5(self, browser):
        faq = TestQuestion(browser)
        faq.go_to_site()
        faq.click_rcc_button()
        faq.check_faq(MainLocators.LOCATOR_MAIN_QUESTION_5)
        faq.find_element(MainLocators.LOCATOR_TEXT_QUESTION_5)

    @allure.suite('Test Вопросы о важном')
    @allure.feature('Test Вы привозите зарядку вместе с самокатом?')
    def test_faq_6(self, browser):
        faq = TestQuestion(browser)
        faq.go_to_site()
        faq.click_rcc_button()
        faq.check_faq(MainLocators.LOCATOR_MAIN_QUESTION_6)
        faq.find_element(MainLocators.LOCATOR_TEXT_QUESTION_6)

    @allure.suite('Test Вопросы о важном')
    @allure.feature('Test Можно ли отменить заказ?')
    def test_faq_7(self, browser):
        faq = TestQuestion(browser)
        faq.go_to_site()
        faq.click_rcc_button()
        faq.check_faq(MainLocators.LOCATOR_MAIN_QUESTION_7)
        faq.find_element(MainLocators.LOCATOR_TEXT_QUESTION_7)

    @allure.suite('Test Вопросы о важном')
    @allure.feature('Test Я жизу за МКАДом, привезёте?')
    def test_faq_8(self, browser):
        faq = TestQuestion(browser)
        faq.go_to_site()
        faq.click_rcc_button()
        faq.check_faq(MainLocators.LOCATOR_MAIN_QUESTION_8)
        faq.find_element(MainLocators.LOCATOR_TEXT_QUESTION_8)
