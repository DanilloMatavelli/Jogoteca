print("SEJA BEM-VINDO AO JOGOTECA!!!")
print("DESENVOLVIDO POR DANILLO!!!")
print("TEMOS OS SEGUINTES JOGOS DISPONÍVEIS")
print("1 - JOGO DA CALCULADORA")
print("2 - JOGO DA FORCA MORTAL")
print("3 - JOGO DA VELHA")

#Validação por idade
idade_jogador = int(input("Qual sua idade:"))
if idade_jogador <18:
    print("Sai daqui muleke, você não é permitido aquii!!")
else:
    print("Pode entrar, você está liberado!!!")
    escolhe_um_jogo = int(input("Qual jogo você deseja jogar?"))
