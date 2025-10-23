#Faça um programa que leia três números e mostre o maior deles

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo numero:  "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 >= numero2 and numero3:
    print("O maior numero é: ",numero1)
elif numero2 >= numero1 and numero2 >= numero3:
    print("O maior número é: ",numero2)
else:
    print("O maior numero é: ",numero3)