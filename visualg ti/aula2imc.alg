algoritmo "calculoIMC"
// Função :
// Autor :
// Data : 21/11/2024
// Seção de Declarações 
var
   nome: caractere
   imc, peso, altura: Real

inicio
// Seção de Comandos 
   Escreval ("Digite o seu nome: ")
   Leia (nome)
   Escreval ("Digite o seu peso: ")
   Leia (peso)
   Escreval ("Digite a sua altura: ")
   Leia (altura)
   imc<- peso / (altura * altura)
   Escreval ("O IMC de ", nome, " é ", imc)
   Escreval ("Tabela de IMC")
   Escreval ("Menor que 18,5: Magreza ")
   Escreval ("Entre 18,5 - 24,9: Normal ")
   Escreval ("Entre 25,0 - 29,9: Sobrepeso ")
   Escreval ("Entre 30,0 - 39,9: Obesidade ")
   Escreval ("Maior que 40,0: Obesidade Grave ")
fimalgoritmo
