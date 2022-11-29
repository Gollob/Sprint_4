from selenium.webdriver.common.by import By


class MainLocators:
    LOCATOR_MAIN_HEADER_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    LOCATOR_MAIN_ORDER_BUTTON = (By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[5]/button[1]")
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