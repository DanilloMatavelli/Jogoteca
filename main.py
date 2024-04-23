import os

os.system("cls")

# Menu Principal
print("SEJA BEM-VINDO AO JOGOTECA!!!")
print("DESENVOLVIDO POR DANILLO!!!")

#Validação por idade
idade_jogador = int(input("Qual sua idade:"))
if idade_jogador <18:
    print("Sai daqui muleke, você não é permitido aquii!!")
else:
    print("Pode entrar, você está liberado!!!")
    print("TEMOS OS SEGUINTES JOGOS DISPONÍVEIS")
    print("1 - JOGO DA CALCULADORA DA MORTE")
    print("2 - JOGO DA FORCA MORTAL")
    print("3 - JOGO DA VELHA ZUMBI")
    escolhe_um_jogo = int(input("Qual jogo você deseja jogar?"))