#Este test se utiliza para iniciar sesion con datos validos 

#Importo las funciones 
from pages.basePage import close_browser, open_chrome
from pages.loginPäge import login

#Creo una funcion para realizar el test a traves de Pytest
def test_login():
    
    #Selecciono el driver que voy a utilizar
    driver = open_chrome()

    #Utilizo la funcion "login" para iniciar sesion 
    login(driver)

    #Cerramos el navegador
    close_browser(driver)
