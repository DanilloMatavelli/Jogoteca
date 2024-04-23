print("Jogo Mortal")
print ("1 -Facil")
print ("2 -Medio")
print ("3 -Dificil")
print ("4 -Senai")

escolha_a_dificuldade = int(input("Digite a dificuldade do jogo:"))

dificuldade_facil = 1
dificuldade_medio = 2
dificuldade_dificil = 3
dificuldade_senai = 4
numero_aleatorio = 0 
import random
digite_um_numero = 0 
quantidade_de_tentativas = 0 
maximo = 0




if escolha_a_dificuldade == 1:
        numero_aleatorio = random.randrange(1,5)
        maximo = 5
if escolha_a_dificuldade == 2:
        numero_aleatorio = random.randrange(1,20)
        maximo = 20
if escolha_a_dificuldade == 3:
        numero_aleatorio = random.randrange(1,50)
        maximo = 50
if escolha_a_dificuldade == 4:
        numero_aleatorio = random.randrange(1,100)
        maximo = 100



    

while numero_aleatorio != digite_um_numero:
    digite_um_numero = int(input("Digite um numero para ver se vc acertou:"))
    quantidade_de_tentativas = quantidade_de_tentativas + 1   
    if quantidade_de_tentativas ==5:
        break
    if digite_um_numero > maximo:
        print("Não tem como, voce é burro??")
    if digite_um_numero < numero_aleatorio:
          print("Dica, o numero é maior ")
    if digite_um_numero > numero_aleatorio:
          print("Dica, o numero é menor ")


    
    


if numero_aleatorio == digite_um_numero:
    print(f"Parabens, voce acertou o numero! , voce precisou de {quantidade_de_tentativas} tentativas")
else:
    print(f"Voce errou, o numero correto era {numero_aleatorio}")
    print(''' 
          /$$$$$$                                           /$$$$$$                               
 /$$__  $$                                         /$$__  $$                              
| $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$       | $$  \ $$ /$$    /$$ /$$$$$$   /$$$$$$ 
| $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$      | $$  | $$|  $$  /$$//$$__  $$ /$$__  $$
| $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$      | $$  | $$ \  $$/$$/| $$$$$$$$| $$  \__/
| $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/      | $$  | $$  \  $$$/ | $$_____/| $$      
|  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$      |  $$$$$$/   \  $/  |  $$$$$$$| $$      
 \______/  \_______/|__/ |__/ |__/ \_______/       \______/     \_/    \_______/|__/      
                                                                                        
                                                                                          
                                                                                          ''')


