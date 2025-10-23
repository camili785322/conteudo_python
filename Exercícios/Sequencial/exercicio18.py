#Faça um programa que peça o tamanho de um arquivo para download
#(em MB) e a velocidade de um link de Internet (em Mbps), calcule e
#informe o tempo aproximado de download do arquivo usando este link
#(em minutos)

tamanho_mb = float(input("Digite o tamanho do arquivo para download em MB:"))
velocidade_Mbps = float(input("Digite a velocidade de um link de internt em Mbps: "))
tamanho = tamanho_mb * 8

tempo_segundo = tamanho / velocidade_Mbps
print("O tempo em segundos é: ",tempo_segundo)

tempo_minuto = tempo_segundo / 60

print("O tempo aproximado de download do arquivo do link em minutos é: ",tempo_minuto)