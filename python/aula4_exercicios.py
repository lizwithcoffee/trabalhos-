# # Idade

idade = 0
idade = int(input("Digite sua idade "))

if idade >= 18:
 print("Você é maior de idade.")

elif idade < 18 and idade > 12:
 print("Você é adolescente.")

else:
 print("Você é criança.")

# Times

time = 0
time = (input("Digite o nome de um time: "))

if ("Internacional , Grêmio , Juventude"):
 print("É um time sulista")

elif ("Corinthians, Palmeiras , São Paulo"):
    print("É um time paulistano")

# Contador de dias

ano= 2025       #formato AAAA
mes=  8        #usar numeros
dia= 7

import datetime

datapadrao = datetime.date(ano, mes, dia)
hoje = datetime.date.today()

if datapadrao > hoje:
    delta = datapadrao - hoje

elif datapadrao <= hoje:
    delta = hoje - datapadrao

print (delta.days)

# Apresentação (nome)

nome = input('Qual é o seu nome? ')
print(f'Olá {nome}, muito prazer.')

# Antecessor e Sucessor

numero = int(input('Informe um número inteiro qualquer: '))
print(f'O antecessor do número {numero} é {numero - 1}, e o sucessor é {numero + 1}')