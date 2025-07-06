# no modificar
def retrieve_phone_code(driver) -> str:
    """Devuelve el código de confirmación de teléfono como string"""
    import json
    import time
    from selenium.common.exceptions import WebDriverException

    for i in range(10):
        try:
            logs = [
                log["message"]
                for log in driver.get_log('performance')
                if log.get("message") and 'api/v1/number?number' in log.get("message")
            ]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody', {
                    'requestId': message_data["params"]["requestId"]
                })
                code = ''.join([x for x in body['body'] if x.isdigit()])
                if code:
                    return code  # ✅ solo devolvemos si encontramos un código
        except WebDriverException:
            time.sleep(1)
            continue

    # ⛔ si no se encontró después de 10 intentos
    raise Exception("No se encontró el código de confirmación del teléfono. Asegúrate de que se haya solicitado correctamente.")
