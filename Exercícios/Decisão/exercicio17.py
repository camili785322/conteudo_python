#Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois
# informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
# O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,uma nota de 5 e quatro notas de 1.

saque = int(input("Digite o valor do saque: "))

qtd_cem = 0
qtd_cinquenta = 0
qtd_vinte = 0
qtd_dez = 0
qtd_cinco = 0
qtd_dois = 0
qtd_um = 0

if saque > 100:
    qtd_cem = saque // 100
    saque = saque - (qtd_cem * 100)

if saque > 50:
    qtd_cinquanta = saque // 50
    saque = saque - (qtd_cinquenta * 50)

if saque > 20:
    qtd_vinte = saque // 20
    saque = saque - (qtd_vinte * 20)

if saque > 10:
    qtd_dez = saque // 10
    saque = saque - (qtd_dez * 10)

if saque > 5:
    qtd_cinco = saque // 5
    saque = saque - (qtd_cinco * 5)

if saque > 2:
    qtd_dois = saque // 2
    saque = saque - (qtd_dois * 2)

if saque > 1:
    qtd_um = saque // 1
    saque = saque - (qtd_um * 1)

print(f"Valor a ser sacado {saque}")
print(f"Notas: ")
print(f"{qtd_cem} notas de 100")
print(f"{qtd_cinquenta} notas de 50")
print(f"{qtd_vinte} notas de 20")
print(f"{qtd_dez} notas de 10")
print(f"{qtd_cinco} notas de 5")
print(f"{qtd_dois} notas de 2")
print(f"{qtd_um} notas de 1")