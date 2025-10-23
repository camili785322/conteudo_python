#Faça um programa que pergunte em que turno você estuda. Peça para digitar:
#M - Matutino
#V - Vespertino
#N - Noturno

turno = input("Digite seu turno: ")

if turno == "M" or turno == "m":
    print("Bom dia")
elif turno == "V" or turno == "v":
    print("Boa tarde")
elif turno == "N" or turno == "n":
    print("Boa noite")
else:
    print("Invalido")