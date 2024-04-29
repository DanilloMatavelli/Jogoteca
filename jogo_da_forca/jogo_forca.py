
from .funções_da_forca import * # Como eu coloquei todas as funções em um outro arquivo, precisei importar tudo

def jogo_da_forca():
    palavra_secreta = escolha_uma_palavra() # Chamei a função escolha_palavra e armezenei o seu retorno


    mascara = cria_mascara_usando_for (palavra_secreta) # CHmaei a função cria_mascara_usando_for passando a palavra secreta 
    print(*mascara)

    # Pergunto ao usuário a letra 
    contador = 0

    while contador < 6:
        letra_escolhia = input("Escolha uma Letra:").upper()
    
        if letra_escolhia not in palavra_secreta:
            contador = contador + 1 

        if contador >= 6 :
            print(palavra_secreta)
            print("Suas vidas acabaram")
            break

        preencher_a_mascara = preenche_mascara (palavra_secreta, letra_escolhia, mascara)
        print(*preencher_a_mascara)

        if "_" not in mascara:
            print("Voce Ganhou!!!")
            break
        input()

        # if len (letra_escolhia) > 1:
        #     letra_escolhia == palavra_secreta
        #     print(palavra_secreta)
        #     print("Você ganhouuu!!!")
        
        # if len (letra_escolhia) != palavra_secreta: 
        #     contador = contador + 2
        #     print("Você perdeu 2 vidas!!!")
        #     break
if "__main__" == __name__:
    jogo_da_forca()    
        





