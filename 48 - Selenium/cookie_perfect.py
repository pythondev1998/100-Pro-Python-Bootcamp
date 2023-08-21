import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/experiments/cookie")


#Get upgrade item ids.
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes


# Definir la duración del temporizador en segundos (5 minutos = 300 segundos)
duration = 300

# Iniciar el temporizador
start_time = time.time()

# Inicializar el tiempo de espera de 5 segundos
timeout = time.time() + 5

while True:
    big_cookie_button = driver.find_element(By.ID, "cookie")
    big_cookie_button.click()

    # Obtener el tiempo transcurrido desde el inicio del temporizador
    elapsed_time = time.time() - start_time

    # Verificar si se ha alcanzado la duración deseada
    if elapsed_time >= duration:
        print("¡Temporizador finalizado!")
        break

    # Imprimir el tiempo transcurrido
    print(f"Tiempo transcurrido: {elapsed_time:.2f} segundos")

    # Verificar si ha pasado un intervalo de 5 segundos
    if time.time() > timeout:

        # Aquí puedes colocar el código que deseas ejecutar cada 5 segundos

        # Obtener todos los elementos <b> de las actualizaciones
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        # Convertir el texto de <b> en un precio entero
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Crear un diccionario de actualizaciones y precios
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Obtener la cantidad actual de cookies
        money_element = driver.find_element(by=By.ID, value="money").text
        cookie_count = int(money_element)

        # Encontrar las actualizaciones que se pueden comprar actualmente
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Comprar la actualización más cara que se pueda permitir
        if affordable_upgrades:
            highest_price_affordable_upgrade = max(affordable_upgrades)
            print(highest_price_affordable_upgrade)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

            driver.find_element(By.ID, to_purchase_id).click()

        # Agregar otros 5 segundos hasta la próxima comprobación
        timeout = time.time() + 5

    # Después de 5 minutos, detener el bot y verificar el recuento de cookies por segundo
    if elapsed_time >= 300:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break