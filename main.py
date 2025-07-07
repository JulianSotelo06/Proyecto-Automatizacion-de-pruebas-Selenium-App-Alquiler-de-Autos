import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from UrbanRoutesPage import UrbanRoutesPage


class TestUrbanRoutes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--start-maximized")

        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        cls.driver = webdriver.Chrome(options=options)
        cls.page = UrbanRoutesPage(cls.driver)

    def test_full_flow(self):
        self.page.open()
        self.page.fill_route_fields()
        self.page.click_request_taxi()
        self.page.select_comfort_tariff()
        self.page.enter_phone_number()
        self.page.enter_confirmation_code()
        self.page.add_card_payment_method()
        self.page.write_message_to_driver()
        self.page.select_blanket_and_tissues()
        self.page.add_ice_creams()
        self.page.confirm_order()
        input("El taxi fue confirmado. Presiona Enter para cerrar.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()













