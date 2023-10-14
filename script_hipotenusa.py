#!/usr/bin/env python3

#Importando biblioteca sys para receber os valores do terminal
#Importando biblioteca math para fazer o calculo de raiz quadrada
import sys
import math

#Recebendo dois valores do terminal
a = sys.argv[1]
b = sys.argv[2]

#Verificando se são valores inteiros
if not (a.isdigit() and b.isdigit()):
    print("Os valores fornecidos devem ser números inteiros")
else:
    a = int(a)
    b = int(b)

#Verificando se os valores são menores que 500
if a >= 500 or b >= 500:
    print("Os números devem ser menores que 500")
else:
    hipotenusa = math.sqrt(a**2 + b**2)
    print(f"O quadrado da hipotenusa para o triangulo retângulo com lados a={a} e b={b}, é {hipotenusa}")


