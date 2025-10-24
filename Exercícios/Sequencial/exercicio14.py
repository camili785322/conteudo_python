#João, um pescador, comprou um microcomputador para controlar o
#rendimento diário de seu trabalho. Toda vez que ele traz um peso de
#peixes maior que o estabelecido pelo regulamento de pesca do estado
#de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo
#excedente. João precisa que você faça um programa que leia a variável
#peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a
#quantidade de quilos além do limite e na variável multa o valor da multa
#que João deverá pagar. Imprima os dados do programa com as
#mensagens adequadas.

<<<<<<< HEAD
valor_peixe = float(input("Digite o peso do peixe: "))

resultado = (valor_peixe - 50) *4
print("O valor da multa por excesso é: ",resultado)
=======
#valor_peixe = float(input("Digite o peso do peixe: "))

#resultado = (valor_peixe - 50) *4
#print("O valor da multa por excesso é: ",resultado)

limite_peso = 50
multa_kg = 4.00

peso_peixe = float(input("Quantos kg de peixe voce pescou?"))

if peso_peixe > limite_peso:
    excedente = peso_peixe - limite_peso
    valor_multa = excedente * multa_kg
    print(f"O excedente é {excedente} kg e o valor da multa é R$ {valor_multa }")
else:
    print(f" Não excedeu o limite de {limite_peso} kg")
excedente = peso_peixe - limite_peso

valor_multa = excedente * multa_kg

print(f"o excedente é {excedente} kg e o valor da multa é R$ {valor_multa}")
>>>>>>> f2348a86c481bb105e4bd4eecd01631635b6fbac
