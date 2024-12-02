# # Média

n1 = n2 = m = 0.0

n1 = float(input("Digite o primeiro valor  "))
n2 = float(input("Digite o segundo valor  "))

m = (n1 + n2) /2
print("A média entre ",n1," e ",n2,"é", m)

# # Ímpar ou par

numero = float(input("Digite um número para saber se é par ou impar: "))
resto = numero % 2

if resto == 0:
    print("Número é par")
else:
    print("Número é impar")

# # Celcius para Fahrenheit

def celsius_fahrenheit():
   c = float(input("Digite a temperatura em °c "))
   f = float((9 * c) / 5) + 32

   return print("A temperatura em fahrenheit: {0}°F".format(f))

celsius_fahrenheit()

# # Fatorial

c = f = n = 0
n = int(input("Digite um número: "))
if (n == 0):
    print(1)
else:
    f = n
    c = 1
    while (c < n):
        f = f * (n-c)
        c = c + 1
    print(f)

# # Palíndromo

def criar_palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    invertido = texto[::-1]
    
    if texto == invertido:
        return True
    else:
        return False

entrada = input("Digite uma palavra ou frase: ")
if criar_palindromo(entrada):
    print("A entrada é um palíndromo!")
else:
    print("A entrada não é um palíndromo!")

# Contar vogais

frase = input("Digite uma palavra/frase: ")
vogais = "aeiou"

frase = frase.lower()

total = 0
for vogal in vogais:
    total += frase.count(vogal)

print("Total: ", total)


# Maior elemento/número

numbers = ['4', '07', '08', '2017', '364', '355673087875675']

print(max(int(number) for number in numbers))  # 355673087875675

# Ordenar em crescente

notas = input("Digite uma sequência de números: ").split()
for n in range(0, len (notas)):
    notas[n] = int(notas[n])
print(notas[n])

maior = 0
for nota in notas:
    if nota > maior:
        maior = nota
print("O maior valor é: ", maior)

# Número primo

number = int(input("Número: "))
ePrimo = 0

for i in range(1, (number + 1)):        
  if number % i == 0:
    ePrimo += 1
    
if ePrimo  == 2 :
  print("O número é primo")
else:
  print("O número não é primo")

# Juros compostos

capital_inicial = float(input("Digite o depósito inicial: R$"))
i = float(input("Agora, digite a taxa de juros de uma poupança: "))
i = (i/100) # Definindo o valor de i separadamente para deixar o código mais limpo
t = 1   # Contador dos meses
aporte = 0 # Não coloque c2. É muito confuso.

while t < 24:
    if t == 1:
        m = capital_inicial + (capital_inicial * i) # Ou: m = capital_inicial * (1 + i)
        print(f'\nNo mês {t}, o valor dos juros será igual a R${m:.2f}')
    else:
        print(f'\nNo mês {t}, o valor dos juros será igual a R${m:.2f}')

    t = t + 1 # Mesma coisa escrever: t += 1

    op = input(f"Deseja realizar um depósito para o {t}° mês[S/N]? ").strip().upper()[0]
    while op != 'S' and op != 'N':
        op = input(f"Opção INVÁLIDA! Deseja realizar um depósito para o {t}° mês[S/N]? ").strip().upper()[0]

    if op == 'S':
        aporte = float(input(f"Digite o valor do depósito do {t}° mês: R$"))
    else:
        aporte = 0
    m = m + (m * i) + aporte # Ou: m = m * (1 + i) + aporte

ganho_com_juros = m - capital_inicial # (montante final - capital inicial)
print(f"No total, a quantidade de reais ganha com os JUROS COMPOSTOS será igual a R${ganho_com_juros}")

    