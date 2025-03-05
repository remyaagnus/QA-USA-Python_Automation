import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_TAXI_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Call a taxi"]')
    SUPPORTIVE_PLAN_LOCATOR = (By.XPATH, '//img[@alt="Supportive"]')
    ACTIVE_TARIFF_CARD_TITLE_LOCATOR = (By.XPATH, '//div[@class="tcard active"]/div[@class="tcard-title"]')
    PHONE_NUMBER_LABEL_LOCATOR = (By.XPATH, '//div[@class="np-text"]')
    PHONE_NUMBER_INPUT_LOCATOR = (By.ID, 'phone')
    PHONE_NUMBER_CODE_LOCATOR = (By.ID, 'code')
    NEXT_LOCATOR = (By.XPATH, '//button[text()="Next"]')
    CONFIRM_LOCATOR = (By.XPATH, '//button[text()="Confirm"]')
    PAYMENT_METHOD_LOCATOR = (By.XPATH, '//div[@class="pp-text"]')
    ADD_CARD_LOCATOR = (By.XPATH, '//div[@class="pp-title" and text()= "Add card"]')
    CARD_NUMBER_LOCATOR = (By.ID, 'number')
    CARD_CODE_LOCATOR = (By.NAME, 'code')
    ADDING_CARD_TITLE_LOCATOR = (By.XPATH, '//div[@class="head" and text()="Adding a card"]')
    LINK_CARD_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Link"]')
    PAYMENT_METHOD_LIST_CLOSE_LOCATOR = (
    By.XPATH, '//div[@class="payment-picker open"]/div/div/button[@class="close-button section-close"]')
    PAYMENT_METHOD_CHECKMARK_LOCATOR = (By.XPATH, '//div[@class="checkmark"]')
    SELECTED_PAYMENT_METHOD_LOCATOR = (By.XPATH, '//div[@class="pp-value-text"]')
    MESSAGE_LOCATOR = (By.ID, 'comment')
    BLANKET_AND_HANDKERCHIEFS_LOCATOR = (By.XPATH, '//div[@class="r-sw"]/div/span')
    BLANKET_AND_HANDKERCHIEFS_INPUT_LOCATOR = (By.XPATH, '//div[@class="r-sw"]/div/input')
    ORDER_BUTTON_LOCATOR = (By.XPATH, '//span[@class="smart-button-main" and text()="Order"]')
    ICE_CREAM_PLUS_LOCATOR = (By.XPATH, '//div[div[text()="Ice cream"]]/div/div/div[@class="counter-plus"]')
    ICE_CREAM_VALUE_LOCATOR = (By.XPATH, '//div[div[text()="Ice cream"]]/div/div/div[@class="counter-value"]')
    ORDER_HEADER_TITLE_LOCATOR = (By.XPATH, '//div[@class="order-header-title"]')

    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    def set_from(self, from_text):
        from_field = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.FROM_LOCATOR))
        from_field.send_keys(from_text)

    def set_to(self, to_text):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def get_from(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_attribute("value")

    def get_to(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_attribute("value")

    def set_route(self, from_text, to_text):
        self.set_from(from_text)
        self.set_to(to_text)

    def book_taxi(self, from_text, to_text):
        self.set_route(from_text, to_text)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.CALL_TAXI_BUTTON_LOCATOR)).click()

    def book_supportive_plan_taxi(self, from_text, to_text):
        self.book_taxi(from_text, to_text)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.SUPPORTIVE_PLAN_LOCATOR)).click()

    def enter_phone_number(self, phone):
        self.driver.find_element(*self.PHONE_NUMBER_LABEL_LOCATOR).click()

        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.PHONE_NUMBER_INPUT_LOCATOR)).send_keys(phone)
        self.driver.find_element(*self.NEXT_LOCATOR).click()

    def enter_phone_code(self, code):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.PHONE_NUMBER_CODE_LOCATOR)).send_keys(code)
        self.driver.find_element(*self.CONFIRM_LOCATOR).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.PHONE_NUMBER_LABEL_LOCATOR).text

    def get_active_tariff_card_title(self):
        return self.driver.find_element(*self.ACTIVE_TARIFF_CARD_TITLE_LOCATOR).text

    def enter_card_details(self, card_number, card_code):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.PAYMENT_METHOD_LOCATOR)).click()

        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.ADD_CARD_LOCATOR)).click()

        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.CARD_NUMBER_LOCATOR)).send_keys(card_number)

        self.driver.find_element(*self.CARD_CODE_LOCATOR).send_keys(card_code)

        self.driver.find_element(*self.ADDING_CARD_TITLE_LOCATOR).click()

        self.driver.find_element(*self.LINK_CARD_BUTTON_LOCATOR).click()

        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.PAYMENT_METHOD_LIST_CLOSE_LOCATOR)).click()

    def get_payment_method(self):
        return self.driver.find_element(*self.SELECTED_PAYMENT_METHOD_LOCATOR).text

    def enter_message_to_driver(self, message):
        self.driver.find_element(*self.MESSAGE_LOCATOR).send_keys(message)

    def get_message_to_driver(self):
        return self.driver.find_element(*self.MESSAGE_LOCATOR).get_attribute("value")

    def order_blankets_handkerchiefs(self):
        self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_LOCATOR).click()

    def get_order_blankets_handkerchiefs_checked(self):
        return self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_INPUT_LOCATOR).is_selected()

    def complete_order(self):
        self.driver.find_element(*self.ORDER_BUTTON_LOCATOR).click()

    def get_order_number(self):
        return self.driver.find_element(*self.ORDER_BUTTON_LOCATOR).text

    def order_ice_creams(self, count):
        # Looping to order necessary count of ice creams
        for number in range(count):
            self.driver.find_element(*self.ICE_CREAM_PLUS_LOCATOR).click()

    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ICE_CREAM_VALUE_LOCATOR).text

    def get_order_title_header(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.ORDER_HEADER_TITLE_LOCATOR)).text
