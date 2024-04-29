print("BEM-VINDO AO JOQUEMPÔ!!!")
print("BORA COMEÇAR A JOGAR!!!")

import random

def joquempô():
    papel = 1
    tesoura = 2
    pedra = 3
    
    #Escolha do usuario

    escolha_o_que_ira_jogar = input("Agora é sua vez de jogar, escolha entre 1- Papel , 2- Tesoura ou 3- Pedra:")

    if escolha_o_que_ira_jogar =="1":
        escolha_o_que_ira_jogar = "Papel"
    if escolha_o_que_ira_jogar =="2":
        escolha_o_que_ira_jogar = "Tesoura"
    if escolha_o_que_ira_jogar =="3":
        escolha_o_que_ira_jogar = "Pedra"
    #Escolha da máquina
    numero_aleatorio = random.randint(1,3)
    if numero_aleatorio == 1:
        numero_aleatorio = "Papel"
    if numero_aleatorio == 2:
        numero_aleatorio = "Tesoura"
    if numero_aleatorio == 3:
        numero_aleatorio = "Pedra"

    print(f"{escolha_o_que_ira_jogar} X {numero_aleatorio}")

    #Verificando as combinações 
    #Combinações vitoria 
    if escolha_o_que_ira_jogar == "Papel" and numero_aleatorio == "Pedra":
        print("Você GANHOUU!!!")
    if escolha_o_que_ira_jogar == "Pedra" and numero_aleatorio == "Tesoura":
        print("Você GANHOUU!!!")
    if escolha_o_que_ira_jogar == "Tesoura" and numero_aleatorio == "Papel":
        print("Você GANHOUU!!!")

    #Combinação Derrota
    if escolha_o_que_ira_jogar == "Pedra" and numero_aleatorio == "Papel":
        print("Você Perdeuu!!!")   
    if escolha_o_que_ira_jogar == "Papel" and numero_aleatorio == "Tesoura":
        print("Você Perdeuu!!!") 
    if escolha_o_que_ira_jogar == "Tesoura" and numero_aleatorio == "Pedra":
        print("Você Perdeuu!!!") 

    #Combinação empate
    if escolha_o_que_ira_jogar == "Pedra" and numero_aleatorio == "Pedra":
        print("Você Perdeuu!!!")   
    if escolha_o_que_ira_jogar == "Papel" and numero_aleatorio == "Papel":
        print("Você Perdeuu!!!") 
    if escolha_o_que_ira_jogar == "Tesoura" and numero_aleatorio == "Tesoura":
        print("Você Perdeuu!!!") 

    input()

if "__main__" == __name__:
    joquempô()













