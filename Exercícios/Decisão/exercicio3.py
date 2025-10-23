#Faça um programa que recebe a informação de sexo da pessoa, e em seguida informa se é Masculino, Feminino, ou Outros,
# sendo que o usuário precisa digitar M para Masculino e F para Feminino.

print("M - Masculino | F - Feminino | O - Outros")
sexo = input("Digite a letra correspondente ao seu sexo: ")

if sexo == "M" or sexo == "m":
    print("Voce é o sexo Masculino")
elif sexo == "F" or sexo == "f":
    print("Voce é o sexo Feminino")
else:
    print("Voce preferiu não informar")

match sexo:
    case "M":
        print("Sexo Masculino")
    case "m":
        print("Sexo Masculino")
    case "F":
        print("Sexo Feminino")
    case "f":
        print("Sexo Feminino")
    case _:
        print("Indefinido")





