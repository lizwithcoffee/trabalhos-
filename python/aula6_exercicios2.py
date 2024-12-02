# Vetor que lê 5 numeros inteiros e mostre-os

listaNumero = []
print ('Informe os 5 numeros')

for i in range(5):
    listaNumero.append(input('numero '+ str(i+1) + ':\n'))
    print (listaNumero) 

# Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa

print ('Informe os 10 numeros reais')
for i in range(10):
	listaNumerosReais.append(float(input('Numero '+ str(i+1) + ':\n')))
listaNumerosReais.reverse()
print (listaNumerosReais)

# Programa que leia 4 notas, mostre as notas e a média na tela

listaNotas = []
media = 0
print ('Informe as 4 notas')
for i in range(4):
	listaNotas.append(float(input('Nota '+ str(i+1) + ':\n')))
	media += listaNotas[i]
media = media/4
print (listaNotas) 
print (media)

# Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

listaChar = []
consoantes = 0
print ('Informe os caracters')
for i in range(10):
	listaChar.append((input('Caracter  '+ str(i+1) + ':\n')))
	char = listaChar[i]
	if(char not in ('a','e','i','o','u')):
		consoantes += 1
print(consoantes)

# Programa que leia 20 números inteiros e armazene-os numa lista. Armazene os números pares na listar PAR e os números IMPARES na lista impar. Imprima os três vetores.

listaPar = []
listaImpar = []
listaNumeros = []
numero = 0
print('Informe os numeros:')
for i in range(20):
	listaNumeros.append((int(input('Numero: ' + str(i+1) + ':\n'))))
	numero = listaNumeros[i]
	print (numero)
	if(numero%2 == 0):
		listaPar.append(numero)
	else:
		listaImpar.append(numero)

print(listaNumeros)
print(listaPar)
print(listaImpar)


#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

listaNotas = []
notasAluno = []
print ('Notas dos Alunos')
for i in range(10):
	media = 0
	notasAluno = []
	print ('Aluno: ' + str(i + 1))
	for j in range(4):
		notasAluno.append(float(input('Nota: ' + str(j+1) + '\n')))
		media += notasAluno[j]
		print (media)
	media = media/4
	listaNotas.append(media)

print (listaNotas)

# Faça um Programa que leia duas listas com 10 elementos cada. Gere uma terceira lista de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados das duas outras listas.

lista1 = []
lista2 = []
listaInter = []

for i in range(10):
	print ('lista 1: ')
	lista1.append(input('Elemento: ' + str(i+1) + '\n'))

for j in range(10):
	print ('lista 2: ')
	lista2.append(input('Elemento: ' + str(i+1) + '\n'))

for m in range(10):
	listaInter.append(lista1[m])
	listaInter.append(lista2[m])


print (lista1)
print (lista2)
print (listaInter)


# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.Calcule a média anual das temperaturas e mostre todas as temperaturas acima da média, em que mês elas ocorreram 
temperatura = []
meses = ['Janeiro','Fevereiro','Março','Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
media = 0
acimaMedia = {}
for i in range(len(meses)):
	temperatura.append(float(input('Informe a Temperatura media de ' + meses[i] + ':\n')))
	media += temperatura[i]
media = media/len(meses)

for i in range(len(meses)):
	if(temperatura[i] > media):
		acimaMedia.update({meses[i] : temperatura[i]})


print('Media das temperaturas : Anual -> ' + str(media))
print('Meses com temperaturas acima da media: ' + str(acimaMedia))
