#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
#que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
#(é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a
#quantidade de horas trabalhadas no mês.
#Desconto do IR: - Salário Bruto até 900 (inclusive) - isento - Salário Bruto até 1500 (inclusive) - desconto de 5% - Salário Bruto até 2500 (inclusive) -
#desconto de 10% - Salário Bruto acima de 2500 - desconto de 20%
#Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é R$5,00 e a quantidade de hora é 220.

valor_hora = float(input("Valor da hora de trabalho: "))
horas_trabalhadas = float(input("Horas trabalhadas no mes: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    percentual_ir = 0.00
elif salario_bruto <= 1500:
    percentual_ir = 0.05
elif salario_bruto <= 2500:
    percentual_ir = 0.10
else:
    percentual_ir = 0.20

percentual_sindicato = 0.03
percentual_FGTS = 0.11

valor_ir = salario_bruto * percentual_ir
valor_INSS = salario_bruto * 0.10
valor_sindicato = salario_bruto * percentual_sindicato
valor_FGTS = salario_bruto * percentual_FGTS

total = valor_ir + valor_sindicato + valor_INSS
salario = salario_bruto - total

print(f"Salário Bruto:({valor_hora} * {horas_trabalhadas}              R$ {salario_bruto:}")
print(f"(-) IR ({percentual_ir}%):                                     R$ {valor_ir:}")
print(f"(-) Sindicato (3%):({percentual_sindicato}                     R$ {valor_sindicato:}")
print(f"FGTS (11% - EMPRESA):({percentual_FGTS}                        R$ {valor_FGTS:}")
print(f"Total de Descontos:                                            R$ {total:}")
print(f"Salário Líquido a Receber:                                     R$ {salario:}")
