#Faça um programa que leia três números e mostre-os em ordem decrescente

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro numero: "))

if n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        print("Ordem decrescente", n1, n2, n3)
    else:
        print("Ordem decrescente:", n1, n2, n3)

elif n2 >= n1 and n2 >= n3:
    if n1 >= n3:
        print("Ordem decrescente:", n1, n2 , n3)
    else:
     print("Ordem decrescente:", n1, n2, n3)
else:
    if n1 >= n2:
        print(" ordem decrescente :", n1, n2, n3)
    else:
        print("Ordem decrescente: ", n1, n2 , n3)