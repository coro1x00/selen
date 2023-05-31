#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# @title ***CHROME***
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Opciones de Chrome
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')

# Ruta del controlador de Chrome
chrome_driver_path = '/content/chromedriver'

# Crear un objeto Service para especificar la ruta del controlador
service = Service(chrome_driver_path)

# Crear una instancia del navegador Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navegar a una página web
driver.get("https://shifu.mrpandabear.org/mine?wallet=002CA3573BA9FB3CEDB451A4D85E5A7D29DF5D2000DCC9AD27")
print(driver.title)
time.sleep (999999)
