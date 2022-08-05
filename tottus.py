from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--star-maximized") # que la ventana emergente aparezca maximizada
options.add_argument("--disable-extensions") # que la ventana de chrome emergente no tenga activada ninguna extensión

# NOTA: se debe urilizar como máximo Google Crome ver. 94.0. El driver no soporta más actualizados. 
driver_path = "C:\\Users\\lukas\\Desktop\\tfinallp2\\chromedriver.exe" # el path en el que se encuentra el driver de chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) # se le coloca el servicio como una clase 
#Servicio sino devuelve error.
driver.get("https://www.tottus.com.pe")

# Para el mensaje pop-up que pregunta si deseamos suscribirnos para ofertas:
## botón con etiqueta button y clase align-right secondary slidedown-button
## NOTA para el TAG se tienen que sustituir los espacios por puntos para que guncione correctamente
## por eso la función replace.

try: 
	WebDriverWait(driver, 10)\
    	.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        	                              'button#onesignal-slidedown-cancel-button.align-right.secondary.slidedown-button')))\
    	.click()
except:
	print("No se llegó a mostrar el mensaje.")


# funcion de hacer click
# el programa espera durante 10 segundos sino se detiene 
#hasta que aparezca el elemento clickeable que es el mensaje de suscripción, le damos click a CANCELAR
# PAra introducir la búsqueda del usuario:

# tag input con id: catalystSearchBar

#producto = input("Introduzca qué producto desea buscar: ")
#print(producto)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#catalystSearchBar')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#inputSearchBar')))\
    .send_keys('rice')

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.jsx-2851002401.searchIcon')))\
    .click()

try: 
	WebDriverWait(driver, 15)\
    	.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        	                              'button.align-right.secondary.slidedown-button')))\
    	.click()
except:
	print("No se llegó a mostrar el mensaje.")