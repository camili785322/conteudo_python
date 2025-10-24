#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A,
# B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2 )/ 2

if media >= 9:
    print("Aprovado")
    print("Conceito A")
elif media >= 7.5:
    print("Aprovado")
    print("Conceito B")
elif media >= 6:
    print("Conceito C")
    print("Aprovado")
elif media >= 4:
    print("Reprovado")
    print("Conceito D")
else:
    print("Reprovado")
    print("Conceito E")

