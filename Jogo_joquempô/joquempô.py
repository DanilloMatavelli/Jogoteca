print("BEM-VINDO AO JOQUEMPÔ!!!")
print("BORA COMEÇAR A JOGAR!!!")

import random

#Escolha do usuario
escolha_o_que_ira_jogar = input("Agora é sua vez de jogar, escolha entre papel , tesoura ou pedra:")

if escolha_o_que_ira_jogar == "papel" :
    papel = 1 
if escolha_o_que_ira_jogar == "tesoura":
    tesoura = 2
if escolha_o_que_ira_jogar == "pedra":
    pedra = 3

#Escolha da máquina
numero_aleatorio = random.randint(1,3)
if numero_aleatorio == 1:
    numero_aleatorio = "papel"
if numero_aleatorio == 2:
    numero_aleatorio = "tesoura"
if numero_aleatorio == 3:
    numero_aleatorio = "pedra"

print(numero_aleatorio)









