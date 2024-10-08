# Arquivo de teste de novas funcionalidades.
import requests
import random

response = requests.get('https://www.ime.usp.br/~pf/dicios/br-utf8.txt')
# print(len(response.text))

new = response.text.split('\n')
random.shuffle(new)
print(new[:20])