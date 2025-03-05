import time

import data
import helpers
from pages import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        # Check if the Urban Routes URL is reachable before running tests
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print('Connected to the Urban Routes server')
        else:
            print('Cannot connect to Urban Routes. Check the server is on and still running')

    def test_set_route(self):
        # Open Urban Routes website
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        # Book a taxi from one address to another
        page.book_taxi(data.ADDRESS_FROM, data.ADDRESS_TO)

        # Verify that the 'from' address is set correctly
        actual_value = page.get_from()
        expected_value = data.ADDRESS_FROM
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

        # Verify that the 'to' address is set correctly
        actual_value = page.get_to()
        expected_value = data.ADDRESS_TO
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    def test_select_plan(self):
        # Open Urban Routes website
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        # Book a taxi with a supportive plan
        page.book_supportive_plan_taxi(data.ADDRESS_FROM, data.ADDRESS_TO)

        # Verify the selected tariff plan
        actual_value = page.get_active_tariff_card_title()
        expected_value = "Supportive"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    def test_fill_phone_number(self):
        # Open Urban Routes website
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        # Book a taxi with a supportive plan
        page.book_supportive_plan_taxi(data.ADDRESS_FROM, data.ADDRESS_TO)

        # Enter phone number
        page.enter_phone_number(data.PHONE_NUMBER)

        # Retrieve and enter phone verification code
        code = helpers.retrieve_phone_code(self.driver)
        page.enter_phone_code(code)

        # Verify that the phone number is correctly entered
        actual_value = page.get_phone_number()
        expected_value = data.PHONE_NUMBER
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    def test_fill_card(self):
        # Open Urban Routes website
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        # Book a taxi with a supportive plan
        page.book_supportive_plan_taxi(data.ADDRESS_FROM, data.ADDRESS_TO)

        # Enter card details
        page.enter_card_details(data.CARD_NUMBER, data.CARD_CODE)

        # Verify the selected payment method
        actual_value = page.get_payment_method()
        expected_value = "Card"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    def test_comment_for_driver(self):
        # Open Urban Routes website
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        # Book a taxi with a supportive plan
        page.book_supportive_plan_taxi(data.ADDRESS_FROM, data.ADDRESS_TO)

        # Enter a comment for the driver
        page.enter_message_to_driver(data.MESSAGE_FOR_DRIVER)

        # Verify the entered message
        actual_value = page.get_message_to_driver()
        expected_value = data.MESSAGE_FOR_DRIVER
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    def test_order_blanket_and_handkerchiefs(self):
        # Open Urban Routes website
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        # Book a taxi with a supportive plan
        page.book_supportive_plan_taxi(data.ADDRESS_FROM, data.ADDRESS_TO)

        # Enter a comment for the driver
        page.enter_message_to_driver(data.MESSAGE_FOR_DRIVER)

        # Order blankets and handkerchiefs
        page.order_blankets_handkerchiefs()

        # Verify that the request was successfully placed
        actual_value = page.get_order_blankets_handkerchiefs_checked()
        assert actual_value

    def test_order_2_ice_creams(self):
        # Open Urban Routes website
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        # Book a taxi with a supportive plan
        page.book_supportive_plan_taxi(data.ADDRESS_FROM, data.ADDRESS_TO)

        # Enter a comment for the driver
        page.enter_message_to_driver(data.MESSAGE_FOR_DRIVER)

        # Order 2 ice creams
        page.order_ice_creams(2)

        # Verify the correct quantity was ordered
        actual_value = page.get_ice_cream_count()
        expected_value = '2'
        assert expected_value == actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    def test_car_search_model_appears(self):
        # Open Urban Routes website
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        # Book a taxi and proceed with order completion
        page.book_supportive_plan_taxi(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.enter_phone_number(data.PHONE_NUMBER)
        code = helpers.retrieve_phone_code(self.driver)
        page.enter_phone_code(code)
        page.enter_message_to_driver(data.MESSAGE_FOR_DRIVER)
        page.complete_order()

        # Verify that the 'Car search' screen appears
        actual_value = page.get_order_title_header()
        expected_value = 'Car search'
        assert expected_value == actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    @classmethod
    def teardown_class(cls):
        # Close the browser after all tests are executed
        cls.driver.quit()
