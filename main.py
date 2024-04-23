import os
from Jogo_da_calculadora.calculadora_extreme import *
from Jogo_da_calculadora.jogo_adivinhacao import * 
from Jogo_da_velha.exercicio_jogo_da_velha import *

os.system("cls")

# Menu Principal
print(" ***** SEJA BEM-VINDO AO JOGOTECA!!! *****")
print(" ***** DESENVOLVIDO POR DANILLO!!!   *****")

#Validação por idade
idade_jogador = int(input("Qual sua idade:"))
if idade_jogador <18:
    print("Sai daqui muleke, você não é permitido aquii!!")
else:
    print("Pode entrar, você está liberado!!!")
    print("TEMOS OS SEGUINTES JOGOS DISPONÍVEIS")
    print("1 - JOGO DA CALCULADORA DA MORTE")
    print("2 - JOGO ADIVINHAÇÃO ")
    print("3 - JOGO DA VELHA ZUMBI")
    print("4 - JOGO DA FORCA MORTAL")
    
    escolhe_um_jogo = int(input("Qual jogo você deseja jogar?"))

    if escolhe_um_jogo ==1: #JOGO DA CALCULADORA
        os.system("cls")
        jogo_calculadora()

    if escolhe_um_jogo ==2:
        os.system("cls")
        jogo_da_adivinhacao()

    if escolhe_um_jogo ==3:
        os.system("cls")
        jogo_da_velha()
    
    


    
