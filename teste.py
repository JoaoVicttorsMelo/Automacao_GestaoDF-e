from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time



opcoes = Options()

# Adicione o argumento "--headless"
opcoes.add_argument("--headless")

# Inicialize o driver do navegador com as opções especificadas
driver = webdriver.Chrome()

# Maximiza a janela do navegador
driver.maximize_window()

# Abra a página de login
driver.get('https://viaveneto.dynamicca.com.br/telas/Login.aspx?xBooAutenticacaoCookie=false')

# Aguarde 5 segundos para o site abrir
time.sleep(2)

# Encontre os campos de nome de usuário e senha e insira suas credenciais
username = driver.find_element(By.ID, 'txtUsuario')
password = driver.find_element(By.ID, 'pwbSenha')
username.send_keys('ti.loja')
password.send_keys('cnxloja01')

# Pressione Enter para fazer login
password.send_keys(Keys.RETURN)

# Aguarde 5 segundos para o site abrir
time.sleep(6)

todos_elementos_div = driver.find_elements(By.TAG_NAME, 'iframe')

print(todos_elementos_div)


driver.close()

