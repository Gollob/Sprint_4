import allure

from locators.locator_main_page import MainLocators
from pages.main_page import TestQuestion

class TestLogo:
    @allure.suite('Провеака логотипов')
    @allure.title('Проверка: если нажать на логотип Яндекса')
    def test_ya_logo(self, browser):
        ya = TestQuestion(browser)
        ya.go_to_site()
        ya.click_rcc_button()
        ya.locator_clicks(MainLocators.LOCATOR_YA_LOGO)
        browser.switch_to.window(browser.window_handles[1])
        assert browser.current_url == 'https://dzen.ru/?yredirect=true'

    @allure.suite('Провеака логотипов')
    @allure.title('Проверка: если нажать на логотип «Самоката»')
    def test_scooter_logo(self, browser):
        scooter = TestQuestion(browser)
        scooter.go_to_site()
        scooter.click_rcc_button()
        scooter.locator_clicks(MainLocators.LOCATOR_MAIN_HEADER_ORDER_BUTTON)
        scooter.locator_clicks(MainLocators.LOCATOR_SCOOTER_LOGO)
        assert browser.current_url == 'https://qa-scooter.praktikum-services.ru/'


class TestHowItWorks:
    @allure.suite('Тест раздела "Вопросы о важном"')
    @allure.title('Проверка выпадающего списока "Сколько это стоит? И как оплатить?"')
    def test_faq_1(self, browser):
        faq = TestQuestion(browser)
        faq.go_to_site()
        faq.click_rcc_button()
        faq.locator_clicks(MainLocators.LOCATOR_MAIN_QUESTION_1)
        faq.find_element(MainLocators.LOCATOR_TEXT_QUESTION_1)

    @allure.suite('Тест раздела "Вопросы о важном"')
    @allure.title('Проверка выпадающего списока "Хочу сразу несколько самокатов! Так можно?"')
    def test_faq_2(self, browser):
        faq = TestQuestion(browser)
        faq.go_to_site()
        faq.click_rcc_button()
        faq.locator_clicks(MainLocators.LOCATOR_MAIN_QUESTION_2)
        faq.find_element(MainLocators.LOCATOR_TEXT_QUESTION_2)

    @allure.suite('Тест раздела "Вопросы о важном"')
    @allure.title('Проверка выпадающего списока "Как рассчитывается время аренды?"')
    def test_faq_3(self, browser):
        faq = TestQuestion(browser)
        faq.go_to_site()
        faq.click_rcc_button()
        faq.locator_clicks(MainLocators.LOCATOR_MAIN_QUESTION_3)
        faq.find_element(MainLocators.LOCATOR_TEXT_QUESTION_3)

    @allure.suite('Тест раздела "Вопросы о важном"')
    @allure.title('Проверка выпадающего списока "Можно ли заказать самокат прямо на сегодня?"')
    def test_faq_4(self, browser):
        faq = TestQuestion(browser)
        faq.go_to_site()
        faq.click_rcc_button()
        faq.locator_clicks(MainLocators.LOCATOR_MAIN_QUESTION_4)
        faq.find_element(MainLocators.LOCATOR_TEXT_QUESTION_4)

    @allure.suite('Тест раздела "Вопросы о важном"')
    @allure.title('Проверка выпадающего списока "Можно ли продлить заказ или вернуть самокат раньше?"')
    def test_faq_5(self, browser):
        faq = TestQuestion(browser)
        faq.go_to_site()
        faq.click_rcc_button()
        faq.locator_clicks(MainLocators.LOCATOR_MAIN_QUESTION_5)
        faq.find_element(MainLocators.LOCATOR_TEXT_QUESTION_5)

    @allure.suite('Тест раздела "Вопросы о важном"')
    @allure.title('Проверка выпадающего списока "Вы привозите зарядку вместе с самокатом?"')
    def test_faq_6(self, browser):
        faq = TestQuestion(browser)
        faq.go_to_site()
        faq.click_rcc_button()
        faq.locator_clicks(MainLocators.LOCATOR_MAIN_QUESTION_6)
        faq.find_element(MainLocators.LOCATOR_TEXT_QUESTION_6)

    @allure.suite('Тест раздела "Вопросы о важном"')
    @allure.title('Проверка выпадающего списока "Можно ли отменить заказ?"')
    def test_faq_7(self, browser):
        faq = TestQuestion(browser)
        faq.go_to_site()
        faq.click_rcc_button()
        faq.locator_clicks(MainLocators.LOCATOR_MAIN_QUESTION_7)
        faq.find_element(MainLocators.LOCATOR_TEXT_QUESTION_7)

    @allure.suite('Тест раздела "Вопросы о важном"')
    @allure.title('Проверка выпадающего списока "Я жизу за МКАДом, привезёте?"')
    def test_faq_8(self, browser):
        faq = TestQuestion(browser)
        faq.go_to_site()
        faq.click_rcc_button()
        faq.locator_clicks(MainLocators.LOCATOR_MAIN_QUESTION_8)
        faq.find_element(MainLocators.LOCATOR_TEXT_QUESTION_8)
