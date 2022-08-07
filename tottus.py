from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import re

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True) # Para que no se cierre el navegador al finalizar el código
options.add_argument("--disable-extensions") # que la ventana de chrome emergente no tenga activada ninguna extensión

# NOTA: se debe urilizar como máximo Google Crome ver. 94.0. El driver no soporta más actualizados. 
driver_path = "C:\\Users\\lukas\\Desktop\\tfinallp2\\chromedriver.exe" # el path en el que se encuentra el driver de chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) # se le coloca el servicio como una clase 
#Servicio sino devuelve error.

driver.get("https://www.tottus.com.pe") # abre el navegador



#####

# Porsipopup es una función que se utilizará después de cada bloque por si acaso aparece una ventana de pop-up que se necesite
# eliminar para que se pueda continuar con el trabajo.

def porsipopup():

# el primer bloque buscará si existe un popup con propaganda de promociones y lo cerrará
  try: 
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                          '/html/body/div[3]/div/div/section/div[2]/a/picture/img')))
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                          '/html/body/div[3]/div/div/section/div[1]/div/button')))\
        .click()
  except:
    print("No se llegó a mostrar el mensaje.")

# el segundo bloque buscará si existe un popup que ofrece suscrpción para descuentos y lo cerrará
  try: 
    WebDriverWait(driver, 5)\
      .until(EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[6]/div')))
    WebDriverWait(driver, 5)\
      .until(EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[6]/div/div/div[2]/button[2]')))\
      .click()
    

  except:
    print("No se llegó a mostrar el mensaje.")

porsipopup()



#####
# funcion de hacer click
# el programa espera durante X segundos sino se detiene 

# Click en la barra de búsqueda

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#catalystSearchBar')))\
    .click()

porsipopup()

# Escribir en la barra de búsqueda

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#inputSearchBar')))\
    .send_keys("arroz") # cambiar a la hora de ejecutar 

porsipopup()

# Click en buscar

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.jsx-2851002401.searchIcon')))\
    .click()





##### 
# Descargar los datos

driver.maximize_window() # maximiza ventana
driver.implicitly_wait(5) # espera para que cargue la página y se puedan descargar datos

titulos = driver.find_element("xpath", "/html/body/div[1]/section/div[1]/section/div[2]/div[2]")
titulos = titulos.text
#print(titulos)

productos2 = re.findall('ARROZ.*', titulos)
print(productos2)
