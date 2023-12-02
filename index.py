from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

service = Service("driver/chromedriver.exe")
bot = webdriver.Chrome(service=service)
actions = ActionChains(bot)
#Maximizar la ventana
bot.maximize_window()
time.sleep(1)

#Abrimos la url indicada
bot.get("https://www.viajesexito.com/")
time.sleep(1)

#ingresar a la opcion Paquetes
paquetes = bot.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[4]/a/p')
time.sleep(1)
#Dar click en el botón buscado
paquetes.click()
time.sleep(1)

#Buscar el campo para ingresar aeropuerto de salida
aeropuestoSalida = bot.find_element(By.ID, 'CityPredictiveFrom_netactica_airhotel')
aeropuestoSalida.click()
time.sleep(1)
#Enviarle el aeropuerto
aeropuerto1 = "José María Cordova"
aeropuestoSalida.send_keys(aeropuerto1)
aeropuestoSalida.send_keys(Keys.ENTER)
time.sleep(2)

aeropuestoLlegada = bot.find_element(By.ID, 'CityPredictiveTo_netactica_airhotel')
aeropuestoLlegada.click()
time.sleep(1)
#Enviarle el aeropuerto
aeropuerto2 = "Punta Cana"
aeropuestoLlegada.send_keys(aeropuerto2)
aeropuestoLlegada.send_keys(Keys.ENTER)
time.sleep(2)

salidaDia = bot.find_element(By.XPATH, '/html/body/div[10]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[2]/div[2]/div[1]')
salidaDia.click()
time.sleep(1)

llegadaDia = bot.find_element(By.XPATH, '/html/body/div[10]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[5]/div[2]/div[1]')
llegadaDia.click()
time.sleep(1)

agregarHabitacion = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/button[1]')
agregarHabitacion.click()
time.sleep(1)

aplicarCambios = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button')
aplicarCambios.click()
time.sleep(1)

buscar = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[4]/a/p')
buscar.click()
time.sleep(1)

primerElemento = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[4]/div/div[4]/div/div[2]/div/p[1]/span[2]').text

print(primerElemento)
time.sleep(1)

opcAvanzadas = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[6]/a')
opcAvanzadas.click()
time.sleep(1)

aerolinea = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input')
aerolinea.click()
time.sleep(1)
#Enviarle el aeropuerto
aerolinea1 = "Avianca"
aerolinea.send_keys(aerolinea1)
aerolinea.send_keys(Keys.ENTER)
time.sleep(2)

buscar2 = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input')
buscar2.click()
time.sleep(1)

whatsapp = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[1]/header/div[1]/div[2]/nav/div/div[1]/a')
whatsapp.click()
time.sleep(1)

#Finaliza el proceso de automatizacion
bot.quit()













 

