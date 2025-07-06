import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import data
# Desde el archivo helpers se importa la función para recibir el código de confirmación del teléfono ingresado.
from helpers import retrieve_phone_code
# Desde el archivo locators se importan los localizadores de los botones que se utilizaran, se importa como "L" para que las líneas de código sean más cortas.
from locators import UrbanRoutesLocators as L

class TestUrbanRoutes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--start-maximized")
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(options=options)

#Prueba para abrir la página de la aplicación al iniciar la pruebas y poderlas visualizar.
    def open_page(self):
        self.driver.get(data.urban_routes_url)
        WebDriverWait(self.driver, 10).until(EC.url_contains("tripleten-services"))
        self.assertIn("tripleten-services", self.driver.current_url)

#No. 1 Prueba para definir las direcciones de la ruta.
    def fill_route_fields(self):
        wait = WebDriverWait(self.driver, 10)
        origin = wait.until(EC.presence_of_element_located(L.FROM_INPUT))
        destination = wait.until(EC.presence_of_element_located(L.TO_INPUT))
        origin.clear()
        origin.send_keys(data.address_from)
        destination.clear()
        destination.send_keys(data.address_to)
        self.assertEqual(origin.get_attribute("value"), data.address_from)
        self.assertEqual(destination.get_attribute("value"), data.address_to)

#No. 2 Prueba para seleccionar la función de Taxi.
    def click_request_taxi(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(L.REQUEST_TAXI_BTN)).click()

#No. 3 Prueba para seleccionar la tarifa de comfort.
    def select_comfort_tariff(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(L.COMFORT_CONTAINER)).click()
        extras_menu = wait.until(EC.visibility_of_element_located(L.BLANKET_LABEL))
        self.assertTrue(extras_menu.is_displayed())

# No. 4 Prueba para ingresar el número de teléfono.
    def enter_phone_number(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(L.PHONE_TRIGGER)).click()
        phone_input = wait.until(EC.presence_of_element_located(L.PHONE_INPUT))
        phone_input.send_keys(data.phone_number)
        self.assertEqual(phone_input.get_attribute("value"), data.phone_number)
        wait.until(EC.element_to_be_clickable(L.NEXT_BUTTON)).click()

# No. 5 Prueba para ingresar código de confirmación al ingresar el número de teléfono.
    def enter_confirmation_code(self):
        wait = WebDriverWait(self.driver, 15)
        code_input = wait.until(EC.presence_of_element_located(L.CODE_INPUT))
        code = retrieve_phone_code(self.driver)
        print(f"Código recibido: {code}")
        code_input.send_keys(code)
        self.assertEqual(code_input.get_attribute("value"), code)
        wait.until(EC.element_to_be_clickable(L.CONFIRM_BUTTON)).click()

# No. 6 Prueba para ingresar la tarjeta como método de pago.
    def add_card_payment_method(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(L.PAYMENT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(L.ADD_CARD_OPTION)).click()
        card_number_input = wait.until(EC.presence_of_element_located(L.CARD_NUMBER_INPUT))
        card_number_input.send_keys(data.card_number)
        self.assertEqual(card_number_input.get_attribute("value"), data.card_number)
        card_code_input = wait.until(EC.presence_of_element_located(L.CARD_CODE_INPUT))
        wait.until(EC.visibility_of(card_code_input))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", card_code_input)
        card_code_input.send_keys(data.card_code)
        card_code_input.send_keys(Keys.TAB)
        wait.until(EC.element_to_be_clickable(L.SUBMIT_CARD_BTN)).click()

        close_buttons = self.driver.find_elements(*L.CLOSE_CARD_WINDOW)
        for btn in close_buttons:
            if btn.is_displayed():
                self.driver.execute_script("arguments[0].click();", btn)
                break

#No. 7 Prueba para escribirle un mensaje al conductor.
    def write_message_to_driver(self):
        wait = WebDriverWait(self.driver, 10)
        message_box = wait.until(EC.presence_of_element_located(L.DRIVER_MESSAGE_INPUT))
        message_box.clear()
        message_box.send_keys(data.message_for_driver)
        self.assertEqual(message_box.get_attribute("value"), data.message_for_driver)

#No. 8 Prueba para seleccionar la manta y los pañuelos.
    def select_blanket_and_tissues(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(L.BLANKET_SWITCH)).click()
        checkbox = self.driver.find_element(*L.BLANKET_CHECKBOX)
        self.assertTrue(checkbox.is_selected())

#No. 9 Prueba para selecionar 2 helados.
    def add_ice_creams(self, count=2):
        wait = WebDriverWait(self.driver, 10)
        plus_button = wait.until(EC.element_to_be_clickable(L.ICECREAM_PLUS_BUTTON))
        for _ in range(count):
            plus_button.click()
        value = wait.until(EC.presence_of_element_located(L.ICECREAM_VALUE))
        self.assertEqual(value.text.strip(), str(count))

#No. 10 Prueba para confirmar el taxi.
    def confirm_order(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(L.CONFIRM_ORDER_BUTTON)).click()
        print("✅ Se hizo clic en el botón para confirmar el pedido")

#Esta función desarrolla las pruebas en orden para poderlas visualizar en el navegador.
    def test_full_flow(self):
        self.open_page()
        self.fill_route_fields()
        self.click_request_taxi()
        self.select_comfort_tariff()
        self.enter_phone_number()
        self.enter_confirmation_code()
        self.add_card_payment_method()
        self.write_message_to_driver()
        self.select_blanket_and_tissues()
        self.add_ice_creams()
        self.confirm_order()
        input("El taxi fue confirmado. Presiona Enter para cerrar.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()









