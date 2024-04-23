import math


def soma(numero1:int, numero2:int):
    resultado = numero1 + numero2
    return resultado
 
def subtracao(numero1:int, numero2:int):
    resultado = numero1 - numero2
    return resultado

def converte_temperatura (graus:str, temperatura: int):
    if graus  == "F":
        F = temperatura * 1.8 + 32
        return F
    else :
        K = temperatura + 273
        return K

def quadrado (A_ou_P : str, lado: int):
    if A_ou_P == "A" :
        A = lado * lado
        return A
    if A_ou_P == "P":
        P = lado + lado + lado + lado
        return P
    
def circulo (A_ou_P : str, raio: int):
    if A_ou_P == "A" :
        A = 3.14 * raio * raio
        return A
    if A_ou_P == "P" : 
        P = 2 * 3.14 * raio
        return P
    
def triangulo (A_ou_P : str, lado_A : int, lado_B : int , lado_C , altura : int):
    if A_ou_P == "A" :
        A = lado_B * altura / 2
        return A 
    if A_ou_P == "P" : 
        P = lado_A + lado_B + lado_C
        return P

def esfera (S_ou_V : str , raio : int):
    if S_ou_V == "S" : 
        S = 4 * 3.14 * raio * raio
        return S
    if S_ou_V == "V" :
        V = 4 * 3.14 * raio **3 / 3
        return  V
    
def retangulo (A_ou_V : str , altura : int , base : int , comprimento :int):
    if A_ou_V == "A" :
        A = 2 * altura * base + 2 * altura * comprimento + 2 * base * comprimento
        return A 
    if A_ou_V == "V" :
        V = altura * base * comprimento
        return V
    
def cone (A_S_ou_V : str , superficie : int , altura : int , raio : int ):
    if A_S_ou_V == "A" : 
        A = 3.14 * raio**2 + 3.14 * raio * (math.sqrt(raio**2 + altura**2))
        return A
    if A_S_ou_V == "S" :
        S = (math.sqrt(raio**2 + altura**2))

    if A_S_ou_V == "V" :
        V = 0.33 / 3.14 * raio**2 * altura
        return V
    
def retangulo (A : str , base : int, altura : int):
    if A == "A" :
        A = base * altura
        return A

def triangulo (A : str , base : int , altura : int ):
    if A == "A" :
        A = base * altura / 2
        return A
    
def trapezio (A : str , base_menor : int , base_maior : int , altura : int ):
    if A =="A" :
        A = (base_menor+base_maior) * altura / 2
        return A
    
