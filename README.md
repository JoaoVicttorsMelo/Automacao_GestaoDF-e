# Projeto de Automação com Selenium

Este projeto utiliza Selenium para automatizar a verificação de contingências em um site específico e enviar um e-mail com os resultados.

![image](https://github.com/JoaoVicttorsMelo/Automacao_GestaoDF-e/assets/69211741/4fd65662-bb97-4b14-ac93-28f13e3a2c8b)


## Dependências

- Selenium
- yagmail
- datetime
- mimetypes

## Como executar

1. Instale as dependências listadas acima.
2. Substitua as credenciais de e-mail e as credenciais do site no script.
3. Execute o script com o comando `python nome_do_script.py`.

## Funcionalidades

O script realiza as seguintes tarefas:

- Verifica se o horário atual está entre 10:30 e 23:00.
- Abre o site em um navegador headless.
- Faz login no site com as credenciais fornecidas.
- Procura por uma imagem específica na página.
- Se a imagem for encontrada, tira uma captura de tela da página.
- Envia um e-mail com a captura de tela como anexo.

## Observações

Este script foi criado para um uso específico e pode não funcionar corretamente em outros sites ou situações. Modifique o código conforme necessário para se adequar às suas necessidades.
