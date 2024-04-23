print("Bem Vindo a Calculadora Extreme!!!")

import random

adição = 1
substração = 2
multiplicação = 3
divisão = 4
operação_matematica = 0

numero_aleatorio = random.randint(1,10)
numero_aleatorio2 = random.randint(1,10)

numero_aleatorio = random.randint(1,4)
if numero_aleatorio ==1:
    soma = numero_aleatorio + numero_aleatorio2
    digite_o_numero = float(input(f"Quanto é {numero_aleatorio} + {numero_aleatorio2}:"))
    if digite_o_numero ==  soma:
        print("Parabens voce acertou!")
    else:
        print(f"Voce errou, é {soma}")
#Substração
if numero_aleatorio ==2:
    substração = numero_aleatorio - numero_aleatorio2
    digite_o_numero = float(input(f"Quanto é {numero_aleatorio} - {numero_aleatorio2}:"))
    if digite_o_numero ==  substração:
        print("Parabens voce acertou!")
    else:
        print(f"Voce errou, é {substração}")
#multiplicação
if numero_aleatorio ==3:
    multiplicação = numero_aleatorio * numero_aleatorio2
    digite_o_numero = float(input(f"Quanto é {numero_aleatorio} * {numero_aleatorio2}:"))
    if digite_o_numero ==  multiplicação:
        print("Parabens voce acertou!")
    else:
        print(f"Voce errou, é {multiplicação}")
#Divisão
if numero_aleatorio ==4:
    divisão = numero_aleatorio / numero_aleatorio2
    divisão = round(divisão, 2)
    digite_o_numero = float(input(f"Quanto é {numero_aleatorio} / {numero_aleatorio2}:"))
    if digite_o_numero ==  divisão:
        print("Parabens voce acertou!")
    else:
        print(f"Voce errou, é {divisão}")


