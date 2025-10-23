import math
#Faça um programa para uma loja de tintas. O programa deverá pedir o
#tamanho em metros quadrados da área a ser pintada. Considere que a
#cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta
#é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao
#usuário a quantidades de latas de tinta a serem compradas e o preço
#total.

metros_quadrados = float(input("Digite o tamanho da area a ser pintada: "))
litro_tinta = math.ceil((metros_quadrados /3 ) /18)
valor = litro_tinta * 80
print("Total de latas de tintas a serem compradas é",litro_tinta,"e o valor total é:",valor)