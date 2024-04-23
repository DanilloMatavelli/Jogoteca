import random

arquivo = open("lista_palavras.txt", "r" , encoding = 'utf8')
lista_palavras = arquivo.read()
arquivo.close()

# palavra_escolhida = random.choice(lista_palavras)
# palavra_escolhida_limpa = palavra_escolhida.strip()

print(lista_palavras)

# OU

# arquivo = open("lista_palavras.txt", "r" , encoding = 'utf8')

# texto_inteiro = arquivo.READ()

# lista= texto_inteiro.split(",")
# print(lista)