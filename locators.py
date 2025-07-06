# Este archivo almacena los localizadores que se van a utilizar en cada función.
from selenium.webdriver.common.by import By

class UrbanRoutesLocators:
    # Localizadores para ingresar las direcciones de la ruta.
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")
    REQUEST_TAXI_BTN = (By.CSS_SELECTOR, "button.button.round")

    # Localizadores para seleccionar la Tarifa Comfort.
    COMFORT_CONTAINER = (By.XPATH, "//img[@alt='Comfort']/..")
    BLANKET_LABEL = (By.XPATH, "//div[contains(@class, 'r-sw-label') and text()='Manta y pañuelos']")
    BLANKET_SWITCH = (By.XPATH, "//div[@class='r-sw-label' and text()='Manta y pañuelos']/following-sibling::div//span[contains(@class, 'slider')]")
    BLANKET_CHECKBOX = (By.XPATH, "//div[@class='r-sw-label' and text()='Manta y pañuelos']/following-sibling::div//input[@type='checkbox']")

    # Localizadores para ingresar el número de Teléfono.
    PHONE_TRIGGER = (By.XPATH, "//div[@class='np-text' and text()='Número de teléfono']")
    PHONE_INPUT = (By.ID, "phone")
    NEXT_BUTTON = (By.CSS_SELECTOR, "button.button.full")
    CODE_INPUT = (By.ID, "code")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(), 'Confirmar')]")

    # Lozalizadores para ingresar la Tarjeta como método de pago.
    PAYMENT_BUTTON = (By.XPATH, "//div[@class='pp-text' and text()='Método de pago']")
    ADD_CARD_OPTION = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    CARD_NUMBER_INPUT = (By.ID, "number")
    CARD_CODE_INPUT = (By.XPATH, "//div[@class='card-code-input']//input[@id='code']")
    SUBMIT_CARD_BTN = (By.XPATH, "//button[@type='submit' and contains(text(), 'Agregar')]")
    CLOSE_CARD_WINDOW = (By.CSS_SELECTOR, "button.close-button.section-close")

    # Lozalizador para escribir el Mensaje al conductor.
    DRIVER_MESSAGE_INPUT = (By.ID, "comment")

    # Localizadores para selecionar los Helados.
    ICECREAM_PLUS_BUTTON = (By.CSS_SELECTOR, "div.counter-plus")
    ICECREAM_VALUE = (By.CSS_SELECTOR, "div.counter-value")

    # Localizar para Confirmar el taxi.
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, "button.smart-button")
