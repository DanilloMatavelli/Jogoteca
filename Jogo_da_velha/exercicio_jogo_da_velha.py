import os 

os.system("cis")

def jogo_da_velha():
    lista_posiçoes = ["1", "2", "3", "4", "5", "6", "7","8", "9"]
    jogador = "O"
    jogadas_disponiveis = 9


    while True:
        while True: #Pergunta a jogada até ser uma jogada válida
            print()
            print(f"{lista_posiçoes[0]:^5} | {lista_posiçoes[1]:^5} | {lista_posiçoes[2]:^5}")
            print(" --------------------")
            print(f"{lista_posiçoes[3]:^5} | {lista_posiçoes[4]:^5} | {lista_posiçoes[5]:^5}")
            print(" --------------------")
            print(f"{lista_posiçoes[6]:^5} | {lista_posiçoes[7]:^5} | {lista_posiçoes[8]:^5}")  
            print()


            print(f"Agora é a vez do jogador {jogador}:")
            jogada = int(input("Faça sua jogada:")) 
            jogada = jogada - 1
        
            jogadas_disponiveis = jogadas_disponiveis + 1 
        
            if lista_posiçoes[jogada ] == "X" or lista_posiçoes[jogada ] == "O":
                print("Jogada Invalida")
            else:
                break
        
        lista_posiçoes[jogada] = jogador
        
        
    

        if jogador == "X" :
            jogador = "O"
        else:
            jogador = "X"

  
    

        if lista_posiçoes[0] == "X" and lista_posiçoes[1] == "X" and lista_posiçoes[2] == "X":
            print("Voce ganhouuu!!!")
            break
        if lista_posiçoes[0] == "O" and lista_posiçoes[1] == "O" and lista_posiçoes[2] == "O":
            print("Voce ganhouuu!!!")
            break
        if lista_posiçoes[3] == "X" and lista_posiçoes[4] == "X" and lista_posiçoes[5] == "X":
            print("Voce ganhouuu!!!")
            break
        if lista_posiçoes[3] == "O" and lista_posiçoes[4] == "O" and lista_posiçoes[5] == "O":
            print("Voce ganhouuu!!!")
            break
        if lista_posiçoes[6] == "X" and lista_posiçoes[7] == "X" and lista_posiçoes[8] == "X":
            print("Voce ganhouuu!!!")
            break
        if lista_posiçoes[6] == "O" and lista_posiçoes[7] == "O" and lista_posiçoes[8] == "O":
            print("Voce ganhouuu!!!")
            break
        if lista_posiçoes[0] == "X" and lista_posiçoes[3] == "X" and lista_posiçoes[6] == "X":
            print("Voce ganhouuu!!!")
            break
        if lista_posiçoes[0] == "O" and lista_posiçoes[3] == "O" and lista_posiçoes[6] == "O":
            print("Voce ganhouuu!!!")
            break
        if lista_posiçoes[1] == "X" and lista_posiçoes[4] == "X" and lista_posiçoes[7] == "X":
            print("Voce ganhouuu!!!")
            break
        if lista_posiçoes[1] == "O" and lista_posiçoes[4] == "O" and lista_posiçoes[7] == "O":
            print("Voce ganhouuu!!!")
            break
        if lista_posiçoes[2] == "X" and lista_posiçoes[5] == "X" and lista_posiçoes[8] == "X":
            print("Voce ganhouuu!!!")
            break
        if lista_posiçoes[2] == "O" and lista_posiçoes[5] == "O" and lista_posiçoes[8] == "O":
            print("Voce ganhouuu!!!")
            break
        if lista_posiçoes[0] == "X" and lista_posiçoes[4] == "X" and lista_posiçoes[8] == "X":
            print("Voce ganhouuu!!!")
            break
        if lista_posiçoes[0] == "O" and lista_posiçoes[4] == "O" and lista_posiçoes[8] == "O":
            print("Voce ganhouuu!!!")
            break
        if lista_posiçoes[2] == "X" and lista_posiçoes[4] == "X" and lista_posiçoes[6] == "X":
            print("Voce ganhouuu!!!")
            break
        if lista_posiçoes[2] == "O" and lista_posiçoes[4] == "O" and lista_posiçoes[6] == "O":
            print("Voce ganhouuu!!!")
            break

        input()


if "__main__" == __name__:
    jogo_da_velha()    
    
  



    

 
   
        


    
