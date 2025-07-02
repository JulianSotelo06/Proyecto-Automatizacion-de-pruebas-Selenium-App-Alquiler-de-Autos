import time

from webdriver_manager.core import driver

import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    pedir_un_taxi_button = (By.XPATH, "//button[text() = 'Pedir un taxi']")
    comfort_button = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Comfort']]")
    phone_number_button = (By.CLASS_NAME, 'np-text')
    phone_number_text = (By.CLASS_NAME, 'label')
    phone_submit_button = (By.CLASS_NAME, "button full")
    phone_code = (By.ID, "code")
    metodo_pago_button = (By.CLASS_NAME, "pp-text")
    tarjeta_button = (By.CLASS_NAME, "pp-title")
    card_number_text = (By.CLASS_NAME, "card-input")
    card_code_text = (By.ID, "code")
    agregar_card_button = (By.CLASS_NAME, "pp-buttons")
    driver_message = (By.CLASS_NAME, "input-container")
    blanket_scarves_button = (By.CLASS_NAME, "switch-input")
    ice_cream_button = (By.CLASS_NAME, "counter-plus")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

#Prueba 1. Configurar direcciones de partida y llegada
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

#Prueba 2. Elegir modo comfort
    def click_pedir_un_taxi_button(self):
        self.driver.find_element(*self.pedir_un_taxi_button).click()
        self.driver.find_element(*self.comfort_button).click()

#Prueba 3. Agregar número de teléfono
    def click_phone_number_button(self):
        self.driver.find_element(*self.phone_number_button).click()
        self.driver.find_element(*self.phone_number_text).send_keys(data.phone_number)
        self.driver.find_element(*self.phone_submit_button).click()
        self.driver.find_element(*self.phone_code).send_keys(retrieve_phone_code(driver))
        self.driver.find_element(*self.phone_submit_button).click()

#Prueba 4. Agregar tarjeta de crédito
    def agregar_tarjeta(self):
        self.driver.get(*self.metodo_pago_button).click()
        self.driver.get(*self.tarjeta_button).click()
        self.driver.get(*self.card_number_text).send_keys(data.card_number)
        self.driver.get(*self.card_code_text).send_keys(data.card_code)
        self.drive.get(*self.agregar_card_button).click()

#Prueba 5. Mensaje para el conductor
    def driver_message_input(self):
        self.driver.get(*self.driver_message).send_keys(data.message_for_driver)

#Prueba 6. Pedir una manta y pañuelos
    def set_blanket_scarves(self):
        self.driver.get(*self.blanket_scarves_button).click()

#Prueba 7. Pedir 2 helados
    def set_ice_cream(self):
        self.driver.get(*self.ice_cream_button).click()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
