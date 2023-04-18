import sys
import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from dados import url_origem

def raspagem():
    try:
        options = Options()
        options.add_argument("force-device-scale-factor=0.25")
        driver = webdriver.Chrome(options=options)
        driver.get(url_origem)

        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.mGAUR')))

        tabelaWeb = driver.find_element(By.CSS_SELECTOR, 'div[role="table"]')
        linhas = tabelaWeb.find_elements(By.CSS_SELECTOR, 'a[role="row"]')

        tabelaRaspagem = []
        i = 0
        hoje = datetime.datetime.now().strftime('%Y-%m-%d')
        for linha in linhas:
            infos = linha.find_elements(By.CLASS_NAME, 'mGAUR')
            tabelaRaspagem.append([])

            for info in infos:
                tabelaRaspagem[i].append(info.get_attribute('innerHTML'))

            
            tabelaRaspagem[i].append(hoje)
            
            #Criar nova lógica para validar informações (regras.txt) 

            i += 1


    finally:
        driver.close()
        return tabelaRaspagem
