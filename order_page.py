import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from base_page import OrederButton


class OrderLocators:
    LOCATOR_ORDER_NAME_FILD = (By.XPATH, "//div[contains(text(),'Введите корректное имя')]")
    LOCATOR_ORDER_LAST_NAME_FILD = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/input[1]")
    LOCATOR_ORDER_ADDRESS_FILD = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[3]/input[1]")
    LOCATOR_ORDER_METRO_SELECTOR = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[4]/div[1]/div[1]/input[1]")
    LOCATOR_ORDER_PHONE_NUMBER_FILD = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[5]/input[1]")
    LOCATOR_ORDER_DATE_FILD = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[5]/input[1]")
    LOCATOR_ORDER_TAME_FILD = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]")
    LOCATOR_ORDER_TAME_OPTION_DAY = (By.XPATH, "//div[contains(text(),'сутки')]")
    LOCATOR_ORDER_COLOR_BLACK_CHECKBOX = (By.CSS_SELECTOR, "#black")
    LOCATOR_ORDER_COLOR_GREY_CHECKBOX = (By.CSS_SELECTOR, "#grey")
    LOCATOR_ORDER_COMMENTS_FILD = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[4]/input[1]")

    LOCATOR_ORDER_NEXT_BUTTON = (By.XPATH, "//button[contains(text(),'Далее')]")
    LOCATOR_ORDER_ORDER_BUTTON = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[3]/button[2]")

    LOCATOR_ORDER_YES_BUTTON = (By.XPATH, "//button[contains(text(),'Да')]")


class InputDate(OrederButton):
    def input_name(self, name):
        name_field = self.find_element(OrderLocators.LOCATOR_ORDER_NAME_FILD)
        name_field.click()
        name_field.send_key(name)
        time.sleep(4)
        return name_field

    def input_last_name(self, last_name):
        last_name_field = self.find_element(OrderLocators.LOCATOR_ORDER_LAST_NAME_FILD)
        last_name_field.click()
        time.sleep(10)
        last_name_field.send_key(last_name)
        time.sleep(10)
        return last_name_field

    def input_address(self, address):
        address_field = self.find_element(OrderLocators.LOCATOR_ORDER_ADDRESS_FILD)
        address_field.click()
        address_field.send_key(address)
        return address_field

    def input_metro(self, metro):
        metro_field = self.find_element(OrderLocators.LOCATOR_ORDER_METRO_SELECTOR)
        metro_field.click()
        metro_field.send_key(metro)
        return metro_field

    def input_phone_number(self, number):
        number_field = self.find_element(OrderLocators.LOCATOR_ORDER_PHONE_NUMBER_FILD)
        number_field.click()
        number_field.send_key(number)
        return number_field

    def input_date(self, date):
        date_field = self.find_element(OrderLocators.LOCATOR_ORDER_DATE_FILD)
        date_field.click()
        date_field.send_key(date)
        return date_field

    def input_tame(self, tame):
        tame_field = self.find_element(OrderLocators.LOCATOR_ORDER_TAME_FILD)
        tame_field.click()
        tame_field = self.find_element(tame)
        tame_field.click()
        return tame_field

    def input_color(self, color_locator):
        color_field = self.find_element(color_locator)
        color_field.click()
        return color_field
