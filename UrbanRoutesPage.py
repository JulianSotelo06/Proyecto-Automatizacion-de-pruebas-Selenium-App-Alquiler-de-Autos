from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import data
from helpers import retrieve_phone_code

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    # Localizadores de los botones y las cajas de texto
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")
    REQUEST_TAXI_BTN = (By.CSS_SELECTOR, "button.button.round")
    COMFORT_CONTAINER = (By.XPATH, "//img[@alt='Comfort']/..")
    BLANKET_LABEL = (By.XPATH, "//div[contains(@class, 'r-sw-label') and text()='Manta y pañuelos']")
    PHONE_TRIGGER = (By.XPATH, "//div[@class='np-text' and text()='Número de teléfono']")
    PHONE_INPUT = (By.ID, "phone")
    NEXT_BUTTON = (By.CSS_SELECTOR, "button.button.full")
    CODE_INPUT = (By.ID, "code")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(), 'Confirmar')]")
    PAYMENT_BUTTON = (By.XPATH, "//div[@class='pp-text' and text()='Método de pago']")
    ADD_CARD_OPTION = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    CARD_NUMBER_INPUT = (By.ID, "number")
    CARD_CODE_INPUT = (By.XPATH, "//div[@class='card-code-input']//input[@id='code']")
    SUBMIT_CARD_BTN = (By.XPATH, "//button[@type='submit' and contains(text(), 'Agregar')]")
    CLOSE_CARD_WINDOW = (By.CSS_SELECTOR, "button.close-button.section-close")
    DRIVER_MESSAGE_INPUT = (By.ID, "comment")
    BLANKET_SWITCH = (By.XPATH, "//div[@class='r-sw-label' and text()='Manta y pañuelos']/following-sibling::div//span[contains(@class, 'slider')]")
    BLANKET_CHECKBOX = (By.XPATH, "//div[@class='r-sw-label' and text()='Manta y pañuelos']/following-sibling::div//input[@type='checkbox']")
    ICECREAM_PLUS_BUTTON = (By.CSS_SELECTOR, "div.counter-plus")
    ICECREAM_VALUE = (By.CSS_SELECTOR, "div.counter-value")
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, "button.smart-button")

    # Métodos para la interacción de las funciones en la página

#Prueba No. 1 Abre la página de Urban Routes
    def open(self):
        self.driver.get(data.urban_routes_url)
        WebDriverWait(self.driver, 10).until(EC.url_contains("tripleten-services"))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FROM_INPUT))
        assert "tripleten-services" in self.driver.current_url

# Prueba No. 2 Establece las direcciones de salida y llegada
    def fill_route_fields(self):
        wait = WebDriverWait(self.driver, 10)
        origin = wait.until(EC.presence_of_element_located(self.FROM_INPUT))
        destination = wait.until(EC.presence_of_element_located(self.TO_INPUT))
        origin.clear()
        origin.send_keys(data.address_from)
        destination.clear()
        destination.send_keys(data.address_to)
        assert origin.get_attribute("value") == data.address_from
        assert destination.get_attribute("value") == data.address_to

# Prueba No. 3 Función para pedir un taxi
    def click_request_taxi(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.REQUEST_TAXI_BTN)).click()

# Prueba No. 4 Selecciona la tarifa comfort
    def select_comfort_tariff(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(self.COMFORT_CONTAINER)).click()
        extras_menu = wait.until(EC.visibility_of_element_located(self.BLANKET_LABEL))
        assert extras_menu.is_displayed()

# Prueba No. 5 Introducir número de teléfono
    def enter_phone_number(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(self.PHONE_TRIGGER)).click()
        phone_input = wait.until(EC.presence_of_element_located(self.PHONE_INPUT))
        phone_input.send_keys(data.phone_number)
        assert phone_input.get_attribute("value") == data.phone_number
        wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON)).click()

# Prueba No. 6 Introducir el código de confirmación del telefóno
    def enter_confirmation_code(self):
        wait = WebDriverWait(self.driver, 15)
        code_input = wait.until(EC.presence_of_element_located(self.CODE_INPUT))
        code = retrieve_phone_code(self.driver)
        print(f"Código recibido: {code}")
        code_input.send_keys(code)
        assert code_input.get_attribute("value") == code
        wait.until(EC.element_to_be_clickable(self.CONFIRM_BUTTON)).click()

# Prueba No. 7 Introducir tarjeta como método de pago
    def add_card_payment_method(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(self.PAYMENT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(self.ADD_CARD_OPTION)).click()
        card_number_input = wait.until(EC.presence_of_element_located(self.CARD_NUMBER_INPUT))
        card_number_input.send_keys(data.card_number)
# ⚠️ Prueba para comprobar el número de la tarjeta
        assert card_number_input.get_attribute("value") == data.card_number
        card_code_input = wait.until(EC.presence_of_element_located(self.CARD_CODE_INPUT))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", card_code_input)
        card_code_input.send_keys(data.card_code)
# ⚠️ Prueba para comprobar el código de la tarjeta (Corrección: Función agregada)
        assert card_code_input.get_attribute("value") == data.card_code
    #Función para activar el botón de agregar la tarjeta
        card_code_input.send_keys(Keys.TAB)
        wait.until(EC.element_to_be_clickable(self.SUBMIT_CARD_BTN)).click()
        card_title = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='pp-title' and text()='Tarjeta']")))
# ⚠️ Prueba para comprobar que la tarjeta fue agregada (Corrección: Función agregada)
        assert card_title.is_displayed(), "❌ No se mostró la tarjeta luego de agregarla."
        close_buttons = self.driver.find_elements(*self.CLOSE_CARD_WINDOW)
        for btn in close_buttons:
            if btn.is_displayed():
                self.driver.execute_script("arguments[0].click();", btn)
                break

# Prueba No. 8 Enviar mensaje al conductor
    def write_message_to_driver(self):
        wait = WebDriverWait(self.driver, 10)
        message_box = wait.until(EC.presence_of_element_located(self.DRIVER_MESSAGE_INPUT))
        message_box.clear()
        message_box.send_keys(data.message_for_driver)
        assert message_box.get_attribute("value") == data.message_for_driver

# Prueba No. 9 Selecionar manta y pañuelos
    def select_blanket_and_tissues(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.BLANKET_SWITCH)).click()
        checkbox = self.driver.find_element(*self.BLANKET_CHECKBOX)
        assert checkbox.is_selected()

# Prueba No. 10 Elegir 2 helados
    def add_ice_creams(self, count=2):
        wait = WebDriverWait(self.driver, 10)
        plus_button = wait.until(EC.element_to_be_clickable(self.ICECREAM_PLUS_BUTTON))
        for _ in range(count):
            plus_button.click()
        value = wait.until(EC.presence_of_element_located(self.ICECREAM_VALUE))
        assert value.text.strip() == str(count)

#Prueba No. 11 Confirmar taxi
    def confirm_order(self):
        wait = WebDriverWait(self.driver, 10)
        confirm_button = wait.until(EC.presence_of_element_located(self.CONFIRM_ORDER_BUTTON))
 # ⚠️ Prueba para comprobar que el modal de Pedir un taxi aparece (Corrección: Función agregada)
        assert "Pedir un taxi" in confirm_button.text, "❌ El botón no contiene el texto esperado."
        wait.until(EC.element_to_be_clickable(self.CONFIRM_ORDER_BUTTON)).click()
        print("✅ Se hizo clic en el botón para confirmar el pedido")

