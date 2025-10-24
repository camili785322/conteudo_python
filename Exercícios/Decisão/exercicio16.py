import math
#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#b. Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
#c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#d. Se o delta for positivo, a equação possui duas raízes reais; informe-as ao usuário;
from re import match

a = float(input("Digite o valor de (a): "))
b = float(input("Digite o valor de (b): "))
c = float(input("Digite o valor de (c): "))

if a == 0:
    print("Essa equação não é de segundo grau")
    exit(1)

delta = b ** 2 - 4 * a * c

if delta <0:
    print("O delta é negativo, portanto não é possível calcular a raiz")


if delta == 0:
    print("O delta possui apenas uma raiz real")
    raiz = 0
    x = b * -1 / (2 * a)
    print(f"O valor de x é: {x}")
else:
    raiz = math.sqrt(delta)
    xa = ((b * -1) + raiz) / (2 * a)
    xb = ((b * -1) + raiz) / (2 * a)
    print(f"O valor de x ' é {xa}")
    print(f"O valor de x ' ' é {xb}")


