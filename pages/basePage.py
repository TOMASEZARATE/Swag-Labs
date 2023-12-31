#Dentro de esta page se colocaran los metodos base para trabajar con los test automatizados

#Importo selenium web driver
from selenium import webdriver
#Importo json
import json

#Esta funcion se utiliza para elegir el driver de Google Chrome
def open_chrome():
    return webdriver.Chrome()

#Esta funcion se utiliza para elegir el driver de Firefox
def open_firefox():
    return webdriver.Firefox()

#Esta funcion se utiliza para elegir el driver de Edge
def open_edge():
    return webdriver.Edge()

#Esta funcion se utiliza para las esperas implicitas 
def implicit_wait(driver):
    driver.implicitly_wait(4) #Defino 4 segundos para encontrar los selectores

#Creo una funcion para abrir la URL
def get_url():
    with open ('data/urlData.json') as archive:
        data = json.load(archive)
        return data.get('url')

#Esta funcion se utiliza para abrir la url 
def open_url(driver):

    #Creo una variable y le asigno la funcion get_url
    url = get_url()
    
    #Abrir url
    driver.get(url)
    
#Esta funcion se utiliza para cerrar el browser
def close_browser(driver):
    driver.quit()
