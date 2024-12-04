# #1) Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

# lista = [1, 2, 3, 4, 5]
# print(lista)
    
# #2) Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

# lista = [1.5, 1.6, 16.4, 4.7, 8.83, 23.43, 9.75, 7.5, 3.65, 0.17]
# lista.reverse()
# print(lista)
    
# #3) Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

# notas = [5.5, 6.5, 7, 9.4]

# print("Notas:", notas,"\nMedia: ", sum(notas) / len(notas))

# #4) Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

# caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# vogais = ['a', 'e', 'i', 'o', 'u']
# count = 0
# while count < 5:
#     if vogais[count] in caracteres:
#         caracteres.remove(vogais[count])
#     count += 1
# print("\nExistem", len(caracteres), "consoantes")
# print("Elas são : ", caracteres)

# #5) Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores

# import random
# numeros = []
# par = []
# impar = []

# for i in range(20):
#     numero_aleatorio = numeros.append(random.randrange(0, 100))

# count = 0
# for i in range(20):
#     if numeros[count] % 2 == 0:
#         par.append(numeros[count])
#     else:
#         impar.append(numeros[count])
#     count += 1

# print("\nNumeros: ", numeros, "\nPares: ", par, "\nImpares: ", impar)

# #6) Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

# notas = []
# media_turma = []

# cont = 1
# for i in range(10):
#     print('\nAluno ',cont)
#     for j in range(4):
#         nota = int(input("Digite a nota: "))
#         notas.append(nota)
#     media = sum(notas) / len(notas)
#     media_turma.append(media)
#     print('\nNotas:', notas,'\nMedia: %.2f'% media)
#     cont += 1
#     notas.clear()

# print('\nMelhores Medias\n')

# for i in range(10):
#     if media_turma[i] >= 7:
#         print('Aluno nº ',i + 1,'Media: ',media_turma[i])

# #7) Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

# from functools import reduce
# numeros = [1, 2, 3, 4, 5]
# multiplicados = reduce((lambda x, y: x * y), numeros)
# print("\nSoma: ", sum(numeros), "\nMultiplicão: ", multiplicados, "\nNúmeros: ", numeros)

# #8) Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

# idade = []
# altura = []
# n_pessoa = 1
# for i in range (5):
#     print('\nPessoa ', n_pessoa)
#     ida = int(input('Digite a idade: '))
#     alt = int(input('Digite a altura: '))
#     idade.append(ida)
#     altura.append(alt)
#     n_pessoa += 1

# idade.reverse()
# altura.reverse()
# print('\nIdade', idade,'\nAltura', altura)

# #9) Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

# import math
# vetor = [1,2,3,4,5,6,7,8,9,10]
# raizes = []

# cont = 0
# for i in range(len(vetor)):
#     raiz = math.sqrt(vetor[cont])
#     raizes.append(raiz)
#     cont += 1

# print('\nRaizes:\n',raizes)
# print('\nSoma:\n',sum(raizes))

# #10) Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# B = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# intercalada = []
# contador = 0
# for i in range(10):
#     intercalada.append(A[contador])
#     intercalada.append(B[contador])
#     contador += 1
# print(intercalada)

# #11) Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# B = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# C = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# intercalada = []
# contador = 0
# for i in range(10):
#     intercalada.append(A[contador])
#     intercalada.append(B[contador])
#     intercalada.append(C[contador])
#     contador += 1
# print(intercalada)

# #12) Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

# import random
# idades = []
# alturas = []
# aluno_13 = []
# media_13 = []

# for i in range(30):
#     numero_aleatorio = idades.append(random.randrange(1, 20))
#     numero_aleatorio2 = alturas.append(random.randrange(50, 200))

# for i in range(30):
#     if idades[i] > 13:
#         aluno_13.append(alturas[i])

# media = sum(aluno_13) / len(aluno_13)

# for i in range(len(aluno_13)):
#     if aluno_13[i] < media:
#         media_13.append(aluno_13[i])

# print('\nA idade dos alunos são:\n',idades,'\nA altura dos alunos em cm são:\n',alturas)
# print('\nForam ',len(aluno_13),' alunos com idade acima de 13 anos que são:\n',aluno_13)
# print('\nA média de altura desses ',len(aluno_13),' alunos é:', media,'cm')
# print('\nForam ',len(media_13),' alunos com mais de 13 anos possuem altura inferior à média de altura:\n',media_13)

# #13) Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

# temperatura_meses = []
# meses = ['Janeiro', 'Fevereiro', 'Março','Abril',
#     'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
#     'Outubro', 'Novembro', 'Dezembro']

# for i in range(12):
#     print('\nMês de ', meses[i], ' :')
#     media = temperatura_meses.append(float(input('Digite a temperatura média: ')))

# media_anual = sum(temperatura_meses) / 12
# print('\n' * 3)
# for i in range(12):
#     if temperatura_meses[i] > media_anual:
#         print('Temperatura a cima da média no mês: ', meses[i])

# #14) Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# #"Telefonou para a vítima?"
# #"Esteve no local do crime?"
# #"Mora perto da vítima?"
# #"Devia para a vítima?"
# #"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

# sim = 0
# perguntas = ['Telefonou para a vitima? [s/n]: ',
#              'Esteve no local do crime? [s/n]: ',
#              'Mora perto da vitima? [s/n]: ',
#              'Devia para a vitima? [s/n]: ',
#              'Já trabalhou com a vítima? [s/n]: '
#              ]
# for i in range(len(perguntas)):
#     resposta = input(perguntas[i])
#     if resposta == 's':
#         sim += 1
# if sim == 2:
#     print('\nSuspeita!')
# elif sim > 2 and sim <= 4:
#     print('\nCumplice!')
# elif sim == 5:
#     print('\nAssassino!')
# else:
#     print('\nInocente!')

# #15) Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# #Mostre a quantidade de valores que foram lidos;
# #Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# #Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# #Calcule e mostre a soma dos valores;
# #Calcule e mostre a média dos valores;
# #Calcule e mostre a quantidade de valores acima da média calculada;
# #Calcule e mostre a quantidade de valores abaixo de sete;
# #Encerre o programa com uma mensagem;

valores = []
media_alta = []
valores_7 = []
cont = 1
rep = True

while rep != 0:
    print('\nValor nº ',cont) 
    val = int(input('Digite o valor: '))
    if val == -1:
       break
    else:
       valores.append(val)
    cont += 1

print('\n' * 2)
print('Quantidade de valores: \n',len(valores))
print('Os valores: \n',valores)
valores.reverse()                #invertendo a lista
print('Os valores na ordem inversa \n',valores)
print('A soma dos valores: \n',sum(valores))

media = sum(valores) / len(valores)
valores.reverse()                #invertendo novamente para a posição original

for i in range(len(valores)):
    if valores[i] > media:
        media_alta.append(valores[i])
    if valores[i] < 7:
        valores_7.append(valores[i])

print('A média dos valores: \n',media)
print('A quantidade de valores acima da média calculada: \n',media_alta)
print('A quantidade de valores abaixo de sete: \n',valores_7)
print('\nPrograma concluido!')

#16) Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
#$200 - $299
#$300 - $399
#$400 - $499
#$500 - $599
#$600 - $699
#$700 - $799
#$800 - $899
#$900 - $999
#$1000 em diante
#Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

possiveis_salarios = [
    [200,299],[300,399],[400,499],
    [500,599],[600,699], [700,799],
    [800,899],[900,999]
    ]
quantidades = [0,0,0,0,0,0,0,0,0]           # pode se usar tambem quantidades = [0] * 9

salarios = []
vendas_brutas = True
while vendas_brutas != 0:
    vendas_brutas = float(input("\nDigite a valor das vendas: "))
    if vendas_brutas == 0:
        break
    else:
        salario = (vendas_brutas * 0.09) + 200
        if salario < 1000:
            for i in range(len(possiveis_salarios)):
                if salario > possiveis_salarios[i][0] and salario < possiveis_salarios[i][1]:
                    quantidades[i] += 1
        else:
            quantidades[8] += 1
print("\n" * 3)
for i in range(len(possiveis_salarios)):
    print("Entre R$", possiveis_salarios[i][0], "e R$", possiveis_salarios[i][1], ":", quantidades[i])
print("Salarios maiores que R$1000:", quantidades[8])

#17) Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta.

nome = True
contador = 1
saltos = []

while nome != 0:
    print('atleta ',contador)
    nome = str(input('Digite o nome do atleta: '))
    if nome == '':
        break
    else:
        for i in range(5):
            print(i + 1,'º Salto')
            distancia = float(input('Digite a distancia em metros do salto: '))
            saltos.append(distancia)    
    media = sum(saltos) / len(saltos)

    print('\nAtleta: ',nome,'\n')

    for i in range(5):
        print(i + 1,'º Salto:' ,saltos[i],'m')

    print('\nResultado final:')
    print('Atleta: ',nome)
    print('Saltos: ',saltos)
    print('Média dos saltos: ',media,'m')
    print('\n' * 3)
    contador += 1

#18) Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
#O total de votos computados;
#Os númeos e respectivos votos de todos os jogadores que receberam votos;
#O percentual de votos de cada um destes jogadores;
#O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
#Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.

votos = []
votos_jogadores_votados = []
numeros_jogadores_votados = []
voto = True
n_voto = 1
while voto != 0:
    print('Voto n°', n_voto)
    voto = int(input('Digite o número do jogador: '))
    if voto == 0:
        break
    else:
        while voto > 23 or voto < 1:
            print('[Voto inválido.]')
            print('Voto n°', n_voto)
            voto = int(input('Digite novamente: '))
        votos.append(voto)
    n_voto += 1
print('\nTotal de votos: ', len(votos))
contador = 1
for i in range(23):
    if contador not in votos:
        contador += 1
        continue
    else:
        votos_jogadores_votados.append(votos.count(contador))
        numeros_jogadores_votados.append(contador)
        print('\nVotos para o jogador camisa n°', contador, ' = ', votos.count(contador))
        print('Percentual de votos: ', round(100 * votos.count(contador) / len(votos), 2), '%')
        contador += 1
melhor = votos_jogadores_votados.index(max(votos_jogadores_votados))
print('\nO jogador mais votado foi o n°', numeros_jogadores_votados[melhor], 'com ', votos_jogadores_votados[melhor], 'votos')
print('Ganhou com', round(100 * votos_jogadores_votados[melhor] / len(votos), 2), '% dos votos')

#19) Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

print(''''Qual o melhor Sistema Operacional para uso em servidores?'

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
''')

urna = []
sistemas = ['Windows Server','Unix','Linux','Netware','Mac OS','Outro']
indice_vitoria = []
indice_porcentagem_vitoria = []
eleitor = True
num_voto = 1

while eleitor != 0:
    print(f'\nEleitor nº {num_voto}\n')
    voto = int(input('Digite o seu voto [1 a 6] ou Digite [0] para sair: '))
    if voto == 0:
        break
    else:
        while voto < 0 or voto > 6:
            print('[Numero Inválido]')
            voto = int(input('Digite o seu voto [1 a 6] ou Digite [0] para sair: '))
        print('[Voto Confirmado]\n')
        urna.append(voto)
    num_voto += 1

print('\n' * 2)
print('{:<19}{:>10}{:>4}'.format('Sistema Operacional','Votos','%'))
print('{:<19}{:>10}{:>6}'.format('-'*19,'-'*5,'-'*3))

contador = 0
for i in range(len(sistemas)):
    porcentagem_voto = round((urna.count(contador+1) / len(urna)) * 100)
    print('{:<19}{:>10}{:>5}%'.format(sistemas[contador],urna.count(contador+1),porcentagem_voto))
    contador +=1
    indice_vitoria.append(urna.count(contador+1))
    indice_porcentagem_vitoria.append(porcentagem_voto)

print('{:<19}{:>10}'.format('-'*19,'-'*5,))
print('{:<19}{:>10}'.format('Total',len(urna)))

vitoria = max(indice_vitoria)
for i in range(len(sistemas)):
    if indice_vitoria[i] == vitoria:
        print('\nO sistema mais votado foi o ', sistemas[i], end=' ')

print('com ', max(indice_vitoria), ' votos, correspondendo a ', max(indice_porcentagem_vitoria), '% dos votos.')

#20) As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
#Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
#Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
#O salário de cada funcionário, juntamente com o valor do abono;
#O número total de funcionário processados;
#O valor total a ser gasto com o pagamento do abono;
#O número de funcionário que receberá o valor mínimo de 100 reais;
#O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.

funcionario = True
salario = []
abono = []

print('Projeção de Gastos com Abono')
print('=' * 28, '\n')

while funcionario != 0:
    valor = float(input('Salario: '))
    if valor == 0:
        break
    salario.append(valor)

print('\nSalário    - Abono')

for i in range(len(salario)):
    percentual = salario[i] * 0.20
    if percentual <= 100:
        percentual = 100
    print('R${:>8.2f} - R${:>8.2f}'.format(salario[i],percentual))
    abono.append(percentual)

val_min = abono.count(100)

print(f'''
Foram processados {len(salario)} colaboradores
Total gasto com abonos: R$ {sum(abono):.2f}
Valor mínimo pago a {val_min} colaboradores
Maior valor de abono pago: R$ {max(abono):.2f}
''')

#21) Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
#O modelo do carro mais econômico;
#Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.

veiculos = ['Fusca', 'Palio', 'UNO', 'Ferrari', 'HB20']
consumo_carros = []

print('\nComparativo de Consumo de Combustível\n')

for i in range(5):
    print('veículo',i + 1,'\nNome: ',veiculos[i])
    km_litro = float(input('Km por litro: '))
    consumo_carros.append(km_litro)

print('\nRelatório Final')

for i in range(5):
    print(f'{i+1} - {veiculos[i]:<15} - {consumo_carros[i]:>6.1f} - {round(1000 / consumo_carros[i]):>5.1f} litros - R$ {round(1000 / consumo_carros[i]) * 2.25:.2f}')

indice_menor_consumo = consumo_carros.index(max(consumo_carros))
print('O menor consumo é o do ', veiculos[indice_menor_consumo])

#22) Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
#Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
#necessita da esfera;
#necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa

defeitos = ['necessita da esfera',
            'necessita de limpeza',
            'necessita troca do cabo ou conector',
            'quebrado ou inutilizado'
            ]
numeros_identificacao = []
numeros_defeitos = []
numero_identificacao = True
n_mouse = 1
while numero_identificacao != 0:
    print('\nMouse n°', n_mouse)
    numero_identificacao = int(input('Digite o número de identificação do mouse: '))
    if numero_identificacao == 0:
        break
    else:
        while numero_identificacao in numeros_identificacao:
            print('[Número repetido]')
            print('\nMouse n°', n_mouse)
            numero_identificacao = int(input('Digite o número de identificação do mouse: '))
        numero_defeito = int(input('Digite o número correspondente ao defeito: '))
        while numero_defeito > 4 or numero_defeito < 1:
            print('[Número invalido]')
            numero_defeito = int(input('Digite o número correspondente ao defeito: '))
        numeros_identificacao.append(numero_identificacao)
        numeros_defeitos.append(numero_defeito)
    n_mouse += 1
print('\nQuantidade de mouses: ', len(numeros_identificacao))
for i in range(len(defeitos)):
    print('Situação: ', defeitos[i], '/ Quantidade: ', numeros_defeitos.count(i + 1), '/ Porcentagem: ', round(100 * numeros_defeitos.count(i + 1) / len(numeros_identificacao), 2), '%')

#23) A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

usuarios = []
uso_dados =[]
uso_dados_MB = []
percentual_MB = []

with open("c:/Users/Suporte/Desktop/Python study/usuarios.txt", 'r') as arquivo: #abrindo o arquivo txt do exercicio é necessario criar o arquivo
    for i in range(6):
        nome = arquivo.readline(15)
        nome = nome.replace(' ','') #remove os espaços em branco
        dados = arquivo.readline(18)
        dados = dados.replace(' ','') #remove os espaços em branco
        dados = int(dados.replace('\n','')) #remove os '\n' e transforma em inteiro
        usuarios.append(nome)
        uso_dados.append(dados)

def conversor_bytes(uso_dados):
    for i in range(len(uso_dados)):
        kilobyte = round(uso_dados[i] / 1024, 2)
        megabyte = round(kilobyte / 1024, 2)
        uso_dados_MB.append(megabyte)
            
def calc_percent(uso_dados_MB):
    for i in range(len(uso_dados_MB)):
        percentual = round(((100 * uso_dados_MB[i]) / sum(uso_dados_MB)), 2)
        percentual_MB.append(percentual)

def impressao(percentual_MB,usuarios):
    with open("c:/Users/Suporte/Desktop/Python study/relatório.txt", 'w') as arquivo: #criando o arquivo relatorio txt
        arquivo.write('ACME Inc.               Uso do espaço em disco pelos usuários\n')
        arquivo.write('-' * 72)
        arquivo.write('\n')
        arquivo.write('Nr.  Usuário        Espaço utilizado     % do uso\n')
        arquivo.write('\n')
        for i in range(len(usuarios)):
            arquivo.write(f'{i+1:<4} {usuarios[i]:<10} {uso_dados_MB[i]:>11} MB {percentual_MB[i]:>17}%\n')
        total = sum(uso_dados_MB)
        media = round(total / len(uso_dados_MB), 2)
        arquivo.write('\n')    
        arquivo.write(f'Espaço total ocupado: {total} MB\nEspaço médio ocupado: {media} MB')

conversor_bytes(uso_dados)
calc_percent(uso_dados_MB)
impressao(percentual_MB,usuarios)

#24) Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados

import random
lancamentos = []
for i in range(100):
    lancamentos.append(random.randrange(1, 6 + 1))
for i in range(6):
    print('O número', i + 1, 'foi gerado ', lancamentos.count(i + 1), 'vezes')   