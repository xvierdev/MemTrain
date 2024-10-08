# Esse projeto se destina ao treinamento da memória em sequências numéricas e alfanuméricas geradas de forma aleatório ou pré determinda.
import random
from os import system, name
from time import sleep

ALPHABET = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
DIGITS = ('0','1', '2', '3', '4', '5', '6', '7', '8', '9')
TIME_DIVISOR = 3
LEVEL_UP = 5

points = 0
difficult = 1

# limpa a tela
def clear_screen():
    system('cls' if name == 'nt' else 'clear')

# cria sequencia aleatória de acordo ao tamanho indicado por lenght
def gen_word(lenght):
    if lenght <= len(ALPHABET) and lenght >= 1:
        letters = list(ALPHABET)
        numbers = list(DIGITS)
        mix = numbers + letters
        random.shuffle(mix)
        new_word = ''.join(mix[:lenght])
        return new_word
    return ''

# incrementador de dificuldade
def increase_dificult():
    if points % LEVEL_UP == 0:
        global difficult
        difficult += 1

# loop principal do jogo
print('Welcome!')
try:
    difficult = int(input('Select the difficulty level (1 ~ 26): '))    
except ValueError:
    print('Invalid value, seting random difficulty ...')
    difficult = random.randint(1,26)
print('Please see the first word!')
sleep(2)

while True:
    word = gen_word(difficult)
    print(word)

    sleep(1 + difficult / TIME_DIVISOR)
    clear_screen()

    answer = input('Whats is the word? ')

    if answer == word:
        points += 1 * difficult
        increase_dificult()
        print(f'Thats right! {points=}')
        sleep(1)
        clear_screen()
    else:
        print(f'Wrong answare {answer=} =/ {word=}')
        print(f'Record {points}')
        points = 0
        difficult = 1
        if input('Continue? y/n: ') == 'n':
            break
        clear_screen()