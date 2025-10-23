nota1 = 5
nota2 = 3
nota3 = 10
nota4 = 8

media = (nota1 + nota2 + nota3 + nota4)/4
print(f"Media {media}")

if media >= 7:
     print("Parabens, voce foi aprovado")
elif media >= 6.5:
    print("Cuidado, voce passou pelo conselho")
elif media >= 2.5:
    print("Voce esta em exame!!!")
else:
    print("Que pena, voce foi reprovado")