#Faça um programa que solicite dois números inteiros e um número real,
#e a partir deles faça:
#a. O produto do dobro do primeiro com a metade do segundo
#b. A soma do triplo do terceiro com o primeiro
#c. O segundo elevado ao cubo

valor1 = int(input("Digite o primeiro numero inteiro"))
valor2 = int(input("Digite o segunto numero inteiro"))
valor3 = float(input("Digite um numero real"))

resultado1 = (valor1 * 2) * valor2/2
print("O dobro do valor1 com a metade do valor2 é:" , resultado1 )

resultado2 = (3 * valor3) + valor1
print("A soma do triplo do valor3 com o valor1 é:  ", resultado2)

resultado3 = valor2 ** 3
print("O valor2 elevado ao cubo é" , resultado3)
