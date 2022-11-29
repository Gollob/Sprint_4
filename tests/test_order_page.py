import allure

from locators.locator_order_page import OrderLocators
from pages.order_page import InputDate


class TestOrder:
    @allure.suite('Тест заказа самоката')
    @allure.title('Проверка заказа самоката через кнопку закать в хедере')
    def test_order_header_order_button(self, browser):
        order = InputDate(browser)
        order.go_to_site()
        order.click_rcc_button()
        order.click_on_header_order_button()
        order.input_name('Олег')
        order.input_last_name('Губа')
        order.input_address('ул. Пушкина 7')
        order.input_metro('Черкизовская')
        order.input_phone_number('89553582585')
        order.locator_clicks(OrderLocators.LOCATOR_ORDER_NEXT_BUTTON)
        order.input_date('22.12.2022')
        order.input_tame(OrderLocators.LOCATOR_ORDER_TAME_OPTION_DAY)
        order.input_color(OrderLocators.LOCATOR_ORDER_COLOR_BLACK_CHECKBOX)
        order.input_comments('hi')
        order.locator_clicks(OrderLocators.LOCATOR_ORDER_ORDER_BUTTON)
        order.locator_clicks(OrderLocators.LOCATOR_ORDER_YES_BUTTON)
        order.find_element(OrderLocators.LOCATOR_ORDER_STATUS_BUTTON)

    @allure.suite('Тест заказа самоката')
    @allure.title('Проверка заказа самоката через кнопку закать')
    def test_order_button(self, browser):
        order = InputDate(browser)
        order.go_to_site()
        order.click_rcc_button()
        order.click_on_order_button()
        order.input_name('Вася')
        order.input_last_name('Пупуин')
        order.input_address('ул. Пушкина 23')
        order.input_metro('Сокольники')
        order.input_phone_number('89783582585')
        order.locator_clicks(OrderLocators.LOCATOR_ORDER_NEXT_BUTTON)
        order.input_date('22.12.2022')
        order.input_tame(OrderLocators.LOCATOR_ORDER_TAME_OPTION_DAY)
        order.input_color(OrderLocators.LOCATOR_ORDER_COLOR_GREY_CHECKBOX)
        order.input_comments('hi')
        order.locator_clicks(OrderLocators.LOCATOR_ORDER_ORDER_BUTTON)
        order.locator_clicks(OrderLocators.LOCATOR_ORDER_YES_BUTTON)
        order.find_element(OrderLocators.LOCATOR_ORDER_STATUS_BUTTON)


