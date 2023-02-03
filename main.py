from selenium import webdriver
import time
import os
import ping3
from selenium.webdriver.common.by import By

fw_path = os.path.abspath("C:\MR50\Firmware.bin")
conf_path = os.path.abspath("C:\MR50\Config.bin")

try:
    if ping3.ping('192.168.1.1') > 0:
        driver = webdriver.Chrome()
        driver.get("http://192.168.1.1")
        driver.implicitly_wait(10)

        #Faz o login na pagina, roteador deve estar resetado
        element = driver.find_elements(By.TAG_NAME, "input")
        element[0].send_keys("alfa1627")
        element[2].send_keys("alfa1627")
        button = driver.find_element(By.TAG_NAME, "a")
        button.click()
        time.sleep(2)

        driver.get("http://192.168.1.1/#firmware")
        time.sleep(1)
        uploadConf = driver.find_element(By.ID, "manual-upgrade-file").find_element(By.TAG_NAME, "input")
        uploadConf.send_keys(fw_path)
        buttonUpgrade = driver.find_element(By.ID, "local-upgrade-btn").find_element(By.TAG_NAME, "a").click()
        confirmButton = driver.find_element(By.ID, "firmware-upgrade-msg-btn-ok").find_element(By.TAG_NAME, "a").click()
        if ping3.ping('192.168.1.1') <= 0:
            driver.close


        if ping3.ping('192.168.1.1') > 0:
            driver = webdriver.Chrome()
            driver.get("http://192.168.1.1")
            driver.implicitly_wait(10)

            element = driver.find_elements(By.TAG_NAME, "input")
            element[0].send_keys("alfa1627")
            # element[2].send_keys("alfa1627")
            button = driver.find_element(By.TAG_NAME, "a")
            button.click()
            time.sleep(1)

            driver.get("http://192.168.1.1/#backupRestore")
            uploadConf = driver.find_element(By.ID, "restore-file").find_element(By.TAG_NAME, "input")
            uploadConf.send_keys(conf_path)
            buttonUpgrade = driver.find_element(By.ID, "restore-button").find_element(By.TAG_NAME, "a").click()
            confirmButton = driver.find_element(By.ID, "restore-confirm-msg-btn-ok").find_element(By.TAG_NAME, "a").click()
            if ping3.ping('192.168.1.1') <= 0:
                driver.close()
                print("Finalizado com sucesso!")

except:
    print("Ocorreu um erro ao processar os dados")
















# # Aguarde até que a página carregue
# driver.implicitly_wait(10)
#
# #abrir a administração
# driver.switch_to.frame(1)
# administration_button = driver.find_element("id", "Fnt_mmManager")
# administration_button.click()
#
# #clica no system
# system_management = driver.find_element("id","smSysMgr")
# system_management.click()
#
# #clica no softwareupgrade
# software_upgrade = driver.find_element("id", "ssmSoftUgr")
# software_upgrade.click()
#
# #clica no escolher arquivo
# escolher_arquivo = driver.find_element("id", "VersionUpload")
# escolher_arquivo.send_keys(file_path)
#
# #upload
# upload_button = driver.find_element("id", "upload")
# upload_button.click()
#
# #confirm
# confirm_button = driver.find_element("id", "msgconfirmb")
# confirm_button.click()
#
# #espera
# time.sleep(49)
# driver.close()
#
# #PASSO 2
# # Crie uma instância do navegador Chrome
# driver = webdriver.Chrome()
#
# # Acesse o IP da ONU ZTE F601
# driver.get("http://192.168.1.1")
#
# # Encontre os elementos de login e senha e preencha-os com seus respectivos valores
# login_element = driver.find_element("name", "Username")
# login_element.send_keys("multipro")
#
# password_element = driver.find_element("name", "Password")
# password_element.send_keys("multipro")
#
# driver.implicitly_wait(10)
# #time.sleep(0.5)
#
# # Encontre o botão de login e clique nele para fazer login
# login_button = driver.find_element("id", "LoginId")
# login_button.click()
#
# # Aguarde até que a página carregue
# driver.implicitly_wait(10)
#
# #abrir a administração
# driver.switch_to.frame(1)
# administration_button = driver.find_element("id", "Fnt_mmManager")
# administration_button.click()
#
# #clica no system
# system_management = driver.find_element("id","smSysMgr")
# system_management.click()
#
# #clica no softwareupgrade
# software_upgrade = driver.find_element("id", "ssmConfMgr")
# software_upgrade.click()
#
# #driver.switch_to.frame(0)
#
# #clica no escolher arquivo
# escolher_arquivo = driver.find_element("id", "ConfigUpload")
# escolher_arquivo.send_keys(config_path)
#
# #upload
# upload_button = driver.find_element("id", "upload")
# upload_button.click()
#
# #confirm
# confirm_button = driver.find_element("id", "msgconfirmb")
# time.sleep(0.5)
# confirm_button.click()
#
# time.sleep(5)
# driver.close()
# input("Finalizado com sucesso")