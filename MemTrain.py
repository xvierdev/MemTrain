# Esse projeto se destina ao treinamento da memória em sequências numéricas e alfanuméricas geradas de forma aleatório ou pré determinda.
import random
import os
import time

ALPHABET = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
points = 0
difficult = 1

# limpa a tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# cria sequencia aleatória de acordo ao tamanho indicado por lenght
def gen_word(lenght):
    if lenght <= len(ALPHABET) and lenght >= 1:
        letters = list(ALPHABET)
        random.shuffle(letters)
        new_word = ''.join(letters[:lenght])
        return new_word
    return ''

# incrementador de dificuldade
def increase_dificult():
    if points % 5 == 0:
        global difficult
        difficult += 1

# loop principal do jogo
print('Welcome!')
print('Please see the first word!')
time.sleep(2)

while True:
    word = gen_word(difficult)
    print(word)

    time.sleep(1 + difficult / 2)
    clear_screen()

    answer = input('Whats is the word? ')

    if answer == word:
        points += 1
        increase_dificult()
        print(f'Thats right! {points=}')
        time.sleep(1)
        clear_screen()
    else:
        print(f'Wrong answare {answer=} =/ {word=}')
        print(f'Record {points}')
        points = 0
        difficult = 1
        if input('Continue? y/n') == 'n':
            break
        clear_screen()