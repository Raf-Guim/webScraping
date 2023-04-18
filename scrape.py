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
            
            #Lógica para garantir que toodos os relatorios tenham 9 colunas
            if len(tabelaRaspagem[i]) == 8:
                if ('%' in tabelaRaspagem[i][3]):
                    #Inserindo valor 0 para LISTAGEM
                    tabelaRaspagem[i].insert(7, '0%')
                else:
                    #Inserindo valor 0 para VARIACÃO
                    tabelaRaspagem[i].insert(3, '0%')
            
            if len(tabelaRaspagem[i]) == 7:
                    #Inserindo valor 0 para LISTAGEM
                    tabelaRaspagem[i].insert(3, '0%')
                    #Inserindo valor 0 para VARIACÃO
                    tabelaRaspagem[i].insert(7, '0%')

            i += 1


    finally:
        driver.close()
        return tabelaRaspagem
