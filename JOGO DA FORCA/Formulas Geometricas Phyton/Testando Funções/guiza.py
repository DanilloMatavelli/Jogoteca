from funções_matematicas import *
import math

# result = soma(8,5)

# print(f"O resultado foi {result} shein")

# temperatura = converte_temperatura("F" , 30)

# print(f" temperatura é {temperatura}")

# area = quadrado("P" , 30)
# print(f" O valor da área do quadrado ou perimetro é {area}")


# area_e_perimetro = circulo ("A" , 5)
# print(f" O valor da área do circulo ou perimetro é {area_e_perimetro}")


# area_e_perimetro = triangulo ("A" , 12 , 4 , 5 , 7 )
# print(f" O valor da área do triangulo ou perimetro é {area_e_perimetro}")

# superficie_e_volume = esfera ("V" , 5)
# print(f"O valor da superficie da esfera ou volume é {superficie_e_volume}")

# area_e_volume = retangulo ("A" , 5 , 9, 7)
# print(f"O valor da área do retangulo ou volume é {area_e_volume}")

# area_superficie_e_volume = cone ("V" ,  9 , 5 , 4)
# print(f"O valor da área, da superficie e do seu volume é {area_superficie_e_volume}")



area_total = triangulo ("A" , 10 ,12 ) + trapezio ("A" , 4 , 12 , 8 ) + retangulo("A" , 24 , 12)
print(area_total)