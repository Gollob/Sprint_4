import time
import allure

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from locators.locator_order_page import OrderLocators
from pages.main_page import OrederButton



class InputDate(OrederButton):

    @allure.step('Ввод имени')
    def input_name(self, name):
        name_field = self.find_element(OrderLocators.LOCATOR_ORDER_NAME_FILD)
        name_field.send_keys(name)
        return name_field

    @allure.step('Ввод фамилии')
    def input_last_name(self, last_name):
        last_name_field = self.find_element(OrderLocators.LOCATOR_ORDER_LAST_NAME_FILD)
        last_name_field.send_keys(last_name)
        return last_name_field

    @allure.step('Ввод адреса')
    def input_address(self, address):
        address_field = self.find_element(OrderLocators.LOCATOR_ORDER_ADDRESS_FILD)
        address_field.send_keys(address)
        return address_field

    @allure.step('Выбор станции метро')
    def input_metro(self, metro):
        metro_field = self.find_element(OrderLocators.LOCATOR_ORDER_METRO_SELECTOR)
        metro_field.send_keys(metro)
        time.sleep(1)
        metro_field.send_keys(Keys.DOWN)
        time.sleep(1)
        metro_field.send_keys(Keys.ENTER)
        time.sleep(1)
        return metro_field

    @allure.step('Ввод тел. номера')
    def input_phone_number(self, number):
        number_field = self.find_element(OrderLocators.LOCATOR_ORDER_PHONE_NUMBER_FILD)
        number_field.send_keys(number)
        return number_field

    @allure.step('Выбор даты')
    def input_date(self, date):
        date_field = self.find_element(OrderLocators.LOCATOR_ORDER_DATE_FILD)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)
        return date_field

    @allure.step('Выбор времени доставки')
    def input_tame(self, tame):
        tame_field = self.find_element(OrderLocators.LOCATOR_ORDER_TAME_FILD)
        tame_field.click()
        time.sleep(1)
        tame_field = self.find_element(tame)
        tame_field.click()
        return tame_field

    @allure.step('Выбор цвета самоката')
    def input_color(self, color_locator):
        color_field = self.find_element(color_locator)
        color_field.click()
        return color_field

    @allure.step('Ввод комента')
    def input_comments(self, comments):
        comments_field = self.find_element(OrderLocators.LOCATOR_ORDER_COMMENTS_FILD)
        comments_field.send_keys(comments)
        return comments_field
