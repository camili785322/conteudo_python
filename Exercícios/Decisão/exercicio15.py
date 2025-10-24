#Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#a. Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#b. Triângulo Equilátero: três lados iguais;
#c. Triângulo Isósceles: quaisquer dois lados iguais;
#d. Triângulo Escaleno: três lados diferentes;

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("O comprimento dos lados de um triângulo deve ser um valor positivo.")
condicao1 = (lado1 + lado2 > lado3)
condicao2 = (lado1 + lado3 > lado2)
condicao3 = (lado2 + lado3 > lado1 )

if condicao1 and condicao2 and condicao3:
    print("Esses valores podem formar um triângulo")

    if lado1 == lado2 and lado2 == lado3:
         print("O triângulo é: EQUILÁTERO (três lados iguais).")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
         print("O triângulo é: ISÓSCELES (pelo menos dois lados iguais).")
    else:
        print("O triângulo é: ESCALENO (três lados diferentes).")
else:
    print("Esses valores não podem formar um triângulo")