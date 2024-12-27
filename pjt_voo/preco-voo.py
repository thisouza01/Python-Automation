# Comparar preços de voo para a Tailandia
# usando Selenium para automação Web para tratar páginas dinâmicas

from selenium import webdriver
import time

# verifica o preço do voo 3 vezes
for _ in range(3):
    # abrir o navegador
    navegador = webdriver.Chrome()

    # ir para a página do google flights
    url = 'https://www.google.com.br/travel/flights/search?tfs=CBwQAhopEgoyMDI1LTAyLTE2ag0IAxIJL20vMDIycGZtcgwIAhIIL20vMGZuMmcaKRIKMjAyNS0wMi0yM2oMCAISCC9tLzBmbjJncg0IAxIJL20vMDIycGZtQAFIAXABggELCP___________wGYAQE&tfu=EgoIABAAGAAgAigB&authuser'
    navegador.get(url)

    time.sleep(5)

    # pegar preço da passagem mais barata
    preco = navegador.find_element('class name', 'jLMuyc').text

    # preço.txt
    with open('preco.txt', 'w') as arquivo:
        arquivo.write(preco)

    time.sleep(5)
