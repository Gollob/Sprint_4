from selenium.webdriver.common.by import By


class OrderLocators:
    LOCATOR_ORDER_NAME_FILD = (By.XPATH, '//*[@placeholder="* Имя"]')
    LOCATOR_ORDER_LAST_NAME_FILD = (By.XPATH, '//*[@placeholder="* Фамилия"]')
    LOCATOR_ORDER_ADDRESS_FILD = (By.XPATH, '//*[@placeholder="* Адрес: куда привезти заказ"]')
    LOCATOR_ORDER_METRO_SELECTOR = (By.XPATH, '//*[@placeholder="* Станция метро"]')
    LOCATOR_ORDER_PHONE_NUMBER_FILD = (By.XPATH, '//*[@placeholder="* Телефон: на него позвонит курьер"]')
    LOCATOR_ORDER_DATE_FILD = (By.XPATH, '//*[@placeholder="* Когда привезти самокат"]')
    LOCATOR_ORDER_TAME_FILD = (By.XPATH, '//div[@class="Dropdown-control"]')
    LOCATOR_ORDER_COLOR_BLACK_CHECKBOX = (By.CSS_SELECTOR, "#black")
    LOCATOR_ORDER_COLOR_GREY_CHECKBOX = (By.CSS_SELECTOR, "#grey")
    LOCATOR_ORDER_COMMENTS_FILD = (By.XPATH, '//*[@placeholder="Комментарий для курьера"]')

    LOCATOR_ORDER_NEXT_BUTTON = (By.XPATH, "//button[contains(text(),'Далее')]")
    LOCATOR_ORDER_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    LOCATOR_ORDER_YES_BUTTON = (By.XPATH, "//button[contains(text(),'Да')]")
    LOCATOR_ORDER_STATUS_BUTTON = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")

    LOCATOR_ORDER_TAME_OPTION_DAY = (By.XPATH, "//div[contains(text(),'трое суток')]")

