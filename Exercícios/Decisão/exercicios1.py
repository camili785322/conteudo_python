#Faça um programa que solicita dois números e imprime o maior deles

numero1 = int(input("Digite um numero inteiro qualquer: "))
numero2 = int(input("Digite outro numero inteir qualquer: "))

if numero1 > numero2:
    print(f"O maior é o {numero1}")
else:
    print(f" O maior é o numero {numero2}")