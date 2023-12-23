#Dentro de esta page se encuentran los elementos de la pagina de Login

#Importo el By
from selenium.webdriver.common.by import By
#Importo json
import json
#Importo las funciones
from pages.basePage import implicit_wait, open_url

#Creo una funcion para leer los datos del archivo "loginData"
def get_credentials():
    with open('data/loginData.json') as archive:
        credentials = json.load(archive)
        return credentials
    
#Creo una funcion para realizar el login 
def login(driver):

    #Importo la funcion open_url 
    open_url(driver)
    
    #Importo la funcion implicit_wait
    implicit_wait(driver)
    
    #Creo una variable y le asigno la funcino get_credentials
    credentials = get_credentials()

    #Obtengo los datos del archivo "loginData"
    user_value = credentials['user']
    password_value = credentials['password']

    #Coloco los selectores de la page Login
    user_selector = driver.find_element(By.ID, "user-name")
    password_selector = driver.find_element(By.ID, "password")
    btn_login = driver.find_element(By.ID, "login-button")

    #Realizo acciones sobre los selectores
    user_selector.send_keys(user_value)
    password_selector.send_keys(password_value)
    btn_login.click()

    #Creo una assercion para validar que se haya ingresado correctamente 
    confirmation = driver.find_element(By.CSS_SELECTOR, "#inventory_filter_container > div")
    message = confirmation.text

    #Mensaje esperado
    expected_message = "Products"

    #Verificar si el mensaje coincide con el esperado
    assert expected_message == message, f"El mensaje no coincide. Esperado: '{expected_message}', Obtenido: '{message}'"

    #Mensaje de confirmacion
    print ('El titulo es el esperado, se confirmo el ingreso dentro de la homePage')
