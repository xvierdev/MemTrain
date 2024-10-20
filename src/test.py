# Arquivo de teste de novas funcionalidades.
import requests
import random

response = requests.get('https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt')
# print(len(response.text))

with open('words.txt', 'w') as words:
    for word in response.text:
        words.write(word)

new = response.text.split('\n')
random.shuffle(new)
print(new[:20])