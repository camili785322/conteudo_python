#Faça um programa que pergunte quanto você ganha por hora e o
#número de horas trabalhadas no mês. Calcule e mostre o total do seu
#salário no referido mês, sabendo-se que são descontados 11% para o
#Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um
#programa que nos dê:
#a. salário bruto.
#b. quanto pagou ao INSS.
#c. quanto pagou ao sindicato.
#d. o salário líquido.

horas = float(input("Digite valor por hora: "))
valor = float(input("Digite o numero de horas trabalhadas"))
imposto_de_renda = 0.11
INSS = 0.08
sindicato = 0.05


resultado_salario_bruto = valor * horas
print("O salario bruto é: ",resultado_salario_bruto)

resultado_imposto_de_renda = resultado_salario_bruto * imposto_de_renda
print("O valor pago de imposto de renda é: ",resultado_imposto_de_renda)

resultado_INSS = resultado_salario_bruto * INSS
print("O valor pago de INSS é: ",resultado_INSS)

resultado_sindicato = resultado_salario_bruto * sindicato
print("O valor pago de sindicato é: ",resultado_sindicato)

<<<<<<< HEAD
salario_liquido = resultado_salario_bruto - resultado_imposto_de_renda - resultado_INSS - resultado_sindicato
=======
salario_liquido = resultado_salario_bruto - resultado_imposto_de_renda - resultado_INSS - resultado_ sindicato
>>>>>>> f2348a86c481bb105e4bd4eecd01631635b6fbac
print("O salario liquido é: ", salario_liquido)



