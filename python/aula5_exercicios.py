# # # Calculador de gastos

gastos_fulano = [15, 50, 230, 340]
gastos_beltrano = [470, 8, 45, 3]

total_gastos_joao = sum(gastos_joao)
total_gastos_pedro = sum(gastos_pedro)

if total_gastos_joao > total_gastos_pedro:
    print("João gastou mais dinheiro este mês.")
elif total_gastos_pedro > total_gastos_joao:
    print("Pedro gastou mais dinheiro este mês.")
else:
    print("João e Pedro gastaram a mesma quantia este mês.")

# # # output:
# # # João gastou mais dinheiro este mês.

# # Menor e maior palavra

palavras = ["python", "java", "swift", "java_script", "powershell"]

maior_palavra = palavras[0]
menor_palavra = palavras[0]

for palavra in palavras:
    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra
    if len(palavra) < len(menor_palavra):
        menor_palavra = palavra

print("A maior palavra é:", maior_palavra)
print("A menor palavra é:", menor_palavra)

# # Segundo maior número

numeros = [61, 10, 72, 87, 55, 11, 26, 51]

numeros.sort()
segundo_maior = numeros[-2]

print("O segundo maior valor da lista é:", segundo_maior)

# # Quantia de votos 

votos = ["C", "B", "A", "C", "C", "A", "C", "C", "B", "A"]

contagem_votos = {}

for produto in votos:
    if produto in contagem_votos:
        contagem_votos[produto] += 1
    else:
        contagem_votos[produto] = 1

print(contagem_votos)

# # Aumento em %

# #No mês passado suas vendas subiram. Então, você calculou a porcentagem  % de aumento vendas e anotou o valor como um número (float) em Python

aumento_vendas = 32.048701

aumento_formatado = "{:.2f}".format(aumento_vendas)
print(f"O aumento percentual de vendas foi de {aumento_formatado}%")

# # Detector de spam

def detectar_spam(email):
    if email.endswith("@xyz.com"):
        print(f"O email de {email} é spam.")
    else:
        print(f"O email de {email} não é spam.")


detectar_spam("usuario1@empresa.com")
# output:
# O email de usuario1@empresa.com não é spam.


detectar_spam("usuario2@xyz.com")
# output:
# O email de usuario2@xyz.com é spam.



 