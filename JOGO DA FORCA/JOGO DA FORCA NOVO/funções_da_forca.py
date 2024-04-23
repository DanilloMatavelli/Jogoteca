#Função responsavel por esolher a palavra secreta
#Por enquanto só retorna uma mesma palavra, mas será alterado
import random

def escolha_uma_palavra() -> str:
    categoria = input("Qual categoria você quer jogar, animais, objetos ou frutas?")
    if categoria == "animais":
        arquivo= open("animais.txt", "r" , encoding = 'utf8')
        categoria_animais = arquivo.read()
        arquivo.close()
        lista = categoria_animais.split("\n")
        palavra_escolhida = random.choice (lista)
        return palavra_escolhida.upper()
    if categoria == "objetos":
        arquivo= open("objetos.txt", "r" , encoding = 'utf8')
        categoria_objetos= arquivo.read()
        arquivo.close()
        lista = categoria_objetos.split("\n")
        palavra_escolhida = random.choice (lista)
        return palavra_escolhida.upper()
    if categoria == "frutas":
        arquivo= open("fruta.txt", "r" , encoding = 'utf8')
        categoria_frutas = arquivo.read()
        arquivo.close()
        lista = categoria_frutas.split("\n")
        palavra_escolhida = random.choice (lista)
        return palavra_escolhida.upper()




    # tupla_de_palavras = ("GATO" , "PATO" , "MATO" , "RINOCERONTE")
    
    # palavra_escolhida = random.choice (tupla_de_palavras)
    # return palavra_escolhida.upper

#Função que retorna uma lista com underline

# def cria_mascara(palavra : str ) -> list:

#     lista_para_a_forca = [] # Eu preciso guardar os numeros para poder imprimi-los depois 
#     contador = 0 # Quantas vezzes vai passar pelo While
   
#     while contador < len("PALMEIRAS"): # Criei o While para repetir sempre quando o numero de letras da pavra for menor que o contador
#         contador = contador + 1 #Eu preciso disso para que o jogo tenha um fim e execute sempre que o numero de letras da palavra for menor que o contador #Cada vez que o loop for executado o contador soma mais um.
#         lista_para_a_forca.append("_")  #Estou guardando os numeros para poder imprimir depois 

#     return lista_para_a_forca #O exercicio pediu para que quando chegasse ao fim ao programa era para imprimir o numero de _ de acordo com o numero de letras da palavra
        


# def cria_mascara(palavra : str ) -> list:
#     lista_mascara = [] #crio uma lista vazia para preencher 

#     num = len(palavra) # Verifico quantas letras tem a palavra, pois isso irá determinar a quantidade de underlines
#     contador = 0

#     while contador <= num:
#         contador = contador + 1 
#         lista_mascara.append("_")

#     return lista_mascara

def cria_mascara_usando_for (palavra:str) -> list:
    lista_mascara = []

    for letra in palavra:
        lista_mascara.append("_")

    return lista_mascara

def preenche_mascara (palavra : str , letra_escolhida : str , mascara : list) -> list:
    lista_posicao = []
    contador_incide = 0 
    
    for letra in palavra :
        if letra == letra_escolhida:
            mascara [contador_incide] = letra_escolhida 
        contador_incide = contador_incide + 1
    return mascara

            


    

