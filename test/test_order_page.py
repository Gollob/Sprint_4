import allure
import time

from selenium import webdriver
from base_page import MainLocators
from order_page import OrderLocators
from order_page import InputDate
from base_page import TestQuestion


class TestOrder():
    def test_order_header_order_button(self, browser):
        order = InputDate(browser)
        order.go_to_site()
        order.click_rcc_button()
        order.click_on_header_order_button()
        # order.input_name('Олег')
        order.input_last_name('Губа')
        # order.input_address('ул. Пушкина 7')
        # order.input_date('22.12.2022')
        # order.input_metro('Черкизовская')
        # order.input_phone_number('89553582585')
        # order.input_date(OrderLocators.LOCATOR_ORDER_TAME_OPTION_DAY)
        # order.input_tame(OrderLocators.LOCATOR_ORDER_COLOR_BLACK_CHECKBOX)


