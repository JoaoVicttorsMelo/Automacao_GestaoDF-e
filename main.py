from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import yagmail
import sys
import time
import datetime
import mimetypes


def verificar_horario():
    # Fuso horário do Brasil (GMT-3)
    horario_atual = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3)))
    # Horário de início (10:30)
    hora_inicio = horario_atual.replace(hour=10, minute=30, second=0, microsecond=0)
    # Horário limite (23:00)
    hora_limite = horario_atual.replace(hour=23, minute=0, second=0, microsecond=0)

    if horario_atual < hora_inicio:
        return False
    elif horario_atual >= hora_limite:
        return False
    else:
        return True


if verificar_horario():

    # Crie uma instância de Options
    opcoes = Options()

    # Adicione o argumento "--headless"
    opcoes.add_argument("--headless")

    # Inicialize o driver do navegador com as opções especificadas
    driver = webdriver.Chrome(options=opcoes)

    # Maximiza a janela do navegador
    driver.maximize_window()

    # Configurações do e-mail e autenticação
    sender_email = 'EMAIL ENVIAR'
    receiver_email = 'EMAIL RECEVER'
    subject = 'NFC-e em Contigência'
    smtp_username = 'EMAIL ENVIAR'
    smtp_password = 'SENHA SMTP'

    # Abra a página de login
    driver.get('URL')

    # Aguarde 5 segundos para o site abrir
    time.sleep(2)

    # Encontre os campos de nome de usuário e senha e insira suas credenciais
    username = driver.find_element(By.ID, 'txtUsuario')
    password = driver.find_element(By.ID, 'pwbSenha')
    username.send_keys('USER')
    password.send_keys('SENHA')

    # Pressione Enter para fazer login
    password.send_keys(Keys.RETURN)

    # Aguarde 3 segundos para o site abrir
    time.sleep(3)
    try:
        # Encontra a imagem com a palavra 'vermelho40' no atributo src
        element = driver.find_element(By.XPATH, '//img[contains(@src, "nfce-vermelho40")]')

        # Clica na imagem
        element.click()

        time.sleep(5)

        screenshot_path = 'screenshot.png'
        driver.save_screenshot(screenshot_path)

        # Lê a imagem como um anexo
        content_type, encoding = mimetypes.guess_type(screenshot_path)
        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'

        yag = yagmail.SMTP(smtp_username, smtp_password)

        content = [
        "<html><body><div style='text-align: center;'>",
        "<p><center><strong style='color: red;'>IMPORTANTE</strong></p>",
        "<p><center>NFC-E em contingência nos estados em anexo:</center></p>",
        "<br><br>",
        "<img src='cid:screenshot'>",
        "</div></body></html>"
    ]

        yag.send(
            to=receiver_email,
            subject=subject,
            contents=content,
            attachments=screenshot_path,
            headers={'X-Priority': '1'},)

        # Encontra a imagem com a palavra 'vermelho40' no atributo src
        elemento = driver.find_element(By.XPATH, '//img[contains(@src, "nfe-vermelho40")]')

        if elemento:
            # Clica na imagem
            element.click()

            time.sleep(5)

            screenshot_path = 'screenshot.png'
            driver.save_screenshot(screenshot_path)

            # Lê a imagem como um anexo
            content_type, encoding = mimetypes.guess_type(screenshot_path)
            if content_type is None or encoding is not None:
                content_type = 'application/octet-stream'

            yag = yagmail.SMTP(smtp_username, smtp_password)

            content = [
                "<html><body><div style='text-align: center;'>",
                "<p><center><strong style='color: red;'>IMPORTANTE</strong></p>",
                "<p><center>NF-E em contingência nos estados em anexo:</center></p>",
                "<br><br>",
                "<img src='cid:screenshot'>",
                "</div></body></html>"
            ]

            yag.send(
                to=receiver_email,
                subject=subject,
                contents=content,
                attachments=screenshot_path,
                headers={'X-Priority': '1'},)

            # Fecha o navegador
            driver.quit()
        else:
            # Fecha o navegador
            driver.quit()
    finally:
        pass
