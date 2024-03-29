#pesquisar #s
#rolar a pagina
#Baixar imagens
from importlib.resources import path
from random import randint
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import wget
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


options = Options()
options.add_experimental_option("detach", True)


options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=C:\\Users\\Bill\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("--headless")

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))


driver.get("https://www.instagram.com/")

hastag_lista = ['gamesbrasil']#lista com as hastag que ele vai trabalhar
tag = -1

for hastag in hastag_lista:#para cada # na lista
    tag=tag+1
    driver.get('https://www.instagram.com/explore/tags/' + hastag_lista[tag] + '/')#entrar na pagina da tag
    wait=WebDriverWait(driver,100)
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")#rolar a pagina para baixo
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")#rolar a pagina para baixo
    time.sleep(4)
    images = driver.find_elements(By.TAG_NAME,'img')
    images = [image.get_attribute('src') for image in images]#encontrando as img

    caminho = 'C:\\Users\\Bill\\Pictures\\0insta' #definindo um caminho para salvar
    #os.mkdir(caminho) #caso precise criar pastas

    counter = 0

    for image in images:#para cada imagem faça...
        if counter > 3:
            salvar = os.path.join(caminho, hastag_lista[tag] + str(counter)+ '.jpg')#escolhendo onde salvar e como ficar o nome do arquivo
            #print(image)
            wget.download(image, salvar)#salvando
        counter +=1    
driver.quit()


