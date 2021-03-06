# Jogo da adivinhação - Estudo

import random

print('Olá! Diga o seu nome.')
name = input()

print('Bom, ' + name + ', eu estou pesando em um número de 1 a 20. Você consegue adivinhar qual é?')
numero = random.randint(1, 20)

for tentativasfeitas in range(1, 7):
    print('Tente adivinhar.')
    tentativa = int(input())

    if tentativa < numero:
        print('Sua tentativa foi abaixo do número que eu pensei.')
    elif tentativa > numero:
        print('Sua tentativa foi acima do número que eu pensei.')
    else:
        break

if tentativa == numero:
    print('Parabéns, ' + name + '! Você acertou o número em ' + str(tentativasfeitas) + ' tentativas!')
else:
    print('Ops... O número que eu pensei foi ' + str(numero))
