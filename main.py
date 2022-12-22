from selenium import webdriver
import time
import os

file_path = os.path.abspath("C:/F601/firmware.bin")
config_path = os.path.abspath("C:/F601/config.bin")


from selenium.webdriver.common.by import By

# Crie uma instância do navegador Chrome
driver = webdriver.Chrome()

# Acesse o IP da ONU ZTE F601
driver.get("http://192.168.1.1")

# Encontre os elementos de login e senha e preencha-os com seus respectivos valores
login_element = driver.find_element("name", "Username")
login_element.send_keys("admin")

password_element = driver.find_element("name", "Password")
password_element.send_keys("admin")

#time.sleep(1)
driver.implicitly_wait(10)

# Encontre o botão de login e clique nele para fazer login
login_button = driver.find_element("id", "LoginId")
login_button.click()

# Aguarde até que a página carregue
driver.implicitly_wait(10)

#abrir a administração
driver.switch_to.frame(1)
administration_button = driver.find_element("id", "Fnt_mmManager")
administration_button.click()

#clica no system
system_management = driver.find_element("id","smSysMgr")
system_management.click()

#clica no softwareupgrade
software_upgrade = driver.find_element("id", "ssmSoftUgr")
software_upgrade.click()

#clica no escolher arquivo
escolher_arquivo = driver.find_element("id", "VersionUpload")
escolher_arquivo.send_keys(file_path)

#upload
upload_button = driver.find_element("id", "upload")
upload_button.click()

#confirm
confirm_button = driver.find_element("id", "msgconfirmb")
confirm_button.click()

#espera
time.sleep(49)
driver.close()

#PASSO 2
# Crie uma instância do navegador Chrome
driver = webdriver.Chrome()

# Acesse o IP da ONU ZTE F601
driver.get("http://192.168.1.1")

# Encontre os elementos de login e senha e preencha-os com seus respectivos valores
login_element = driver.find_element("name", "Username")
login_element.send_keys("multipro")

password_element = driver.find_element("name", "Password")
password_element.send_keys("multipro")

driver.implicitly_wait(10)
#time.sleep(0.5)

# Encontre o botão de login e clique nele para fazer login
login_button = driver.find_element("id", "LoginId")
login_button.click()

# Aguarde até que a página carregue
driver.implicitly_wait(10)

#abrir a administração
driver.switch_to.frame(1)
administration_button = driver.find_element("id", "Fnt_mmManager")
administration_button.click()

#clica no system
system_management = driver.find_element("id","smSysMgr")
system_management.click()

#clica no softwareupgrade
software_upgrade = driver.find_element("id", "ssmConfMgr")
software_upgrade.click()

#driver.switch_to.frame(0)

#clica no escolher arquivo
escolher_arquivo = driver.find_element("id", "ConfigUpload")
escolher_arquivo.send_keys(config_path)

#upload
upload_button = driver.find_element("id", "upload")
upload_button.click()

#confirm
confirm_button = driver.find_element("id", "msgconfirmb")
time.sleep(0.5)
confirm_button.click()

time.sleep(5)
driver.close()
input("Finalizado com sucesso")