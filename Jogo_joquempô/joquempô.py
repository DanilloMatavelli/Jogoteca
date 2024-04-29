print("BEM-VINDO AO JOQUEMPÔ!!!")
print("BORA COMEÇAR A JOGAR!!!")

import random

papel = 1
tesoura = 2
pedra = 3
#Escolha do usuario

escolha_o_que_ira_jogar = input("Agora é sua vez de jogar, escolha entre 1- Papel , 2- Tesoura ou 3- Pedra:").upper()

if escolha_o_que_ira_jogar =="1":
    escolha_o_que_ira_jogar = "Papel"
if escolha_o_que_ira_jogar =="2":
    escolha_o_que_ira_jogar = "Tesoura"
if escolha_o_que_ira_jogar =="3":
    escolha_o_que_ira_jogar = "Pedra"
#Escolha da máquina
numero_aleatorio = random.randint(1,3)
if numero_aleatorio == 1:
    numero_aleatorio = "papel"
if numero_aleatorio == 2:
    numero_aleatorio = "tesoura"
if numero_aleatorio == 3:
    numero_aleatorio = "pedra"

print(numero_aleatorio)

#Verificando as combinações 











