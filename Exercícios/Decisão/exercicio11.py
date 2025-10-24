4#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um
#colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#a. salários até R$ 1.450,00 (incluindo): aumento de 20%
#b. salários entre R$ 1.451,00 e R$ 2.800,00: aumento de 15%
#c. salários entre R$ 2.800,00 e R$ 3.500,00: aumento de 10%
#d. salários de R$ 3.500,00 em diante: aumento de 5%
#Após o aumento ser realizado, informe na tela:
#e. o salário antes do reajuste;
#f. o percentual de aumento aplicado;
#g. o valor do aumento;
#h. o novo salário, após o aumento.

salario = float(input("Digite seu salario bruto: "))

if salario <= 1450:
     percentual = 0.20
elif salario <= 2800:
     percentual = 0.15
elif salario <= 3500:
    percentual = 0.10
else:
    percentual = 0.5

aumento = salario * percentual
salario_novo = salario + aumento
percentual = (percentual * 100)

print("Salario antes do reajuste: ", salario)
print("O percentual de aumento aplicado:", percentual)
print("O valor do aumento: ",aumento)
print("O novo salario é: ", salario_novo)

