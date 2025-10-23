#Operadores matemáticos
import math

# + <- Soma: soma o valor da esquerda com o da direita
# - <- Subtração: subtrai o valor da esquerda pelo da direita
# * <- Multiplicação: multiplica o valor da esquerda com o da direita
# \ <- Divisão: divide o valor da esquerda pelo da direita

# ** <- Potencia: eleva o valor da esquerda pelo da direita
# Math. sqrt(valor) <- raiz quadrada: tira a raiz quadrada do valor

# // <- Inteiro da divisão: Quando faz uma divisão que resulta em
# valor float, retorna so a parte inteira. 10.56 retornaria apenas 10

# % <- Resto da divisão: Retorna o valor de resto quando a divisão
# naõ é exata. 5/2 teria o resto 1. Útil na indentificação de valores par

valor_1 = int(input ("Digite o valor 1: "))
valor_2 = int(input("Digite o valor 2 : "))

print("Os valores digitados são:",valor_1,"e", valor_2)

resultado = valor_1 + valor_2
print(" A soma dos dois valores é:",resultado)

resultado = valor_1 - valor_2
print("A subtração dos dois valores é:",resultado)

resultado = valor_1 * valor_2
print("A multiplicação do dois valores é:",resultado)

resultado = valor_1 / valor_2
print("A divisão dos dois valores é:",resultado)

resultado = valor_1 // valor_2
print("A divisão com resultados inteiros dos dois valores são:",resultado)
resultado = valor_1 ** valor_2
print("A potencia dos dois valores é:",resultado)

resultado = valor_1 % valor_2
print("O resto da divião dos dois valores é:",resultado)

resultado = math.sqrt(valor_1)
print("A raiz quadrada do valor_1:",valor_1 ,"e", resultado)

resultado = math.sqrt(valor_2)
print("A raiz quadrada do valor_2: ",valor_2,"e",resultado)

print("O valor de pi é:",math.pi)