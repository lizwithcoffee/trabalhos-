algoritmo "aula3fibonacci"
// Função :
// Autor :
// Data : 22/11/2024
// Seção de Declarações 
var
   ant, atual, numAux, cont, valor:inteiro

inicio
// Seção de Comandos
   Escreval("Digite um valor para calculo: ", valor)
   Leia(valor)
   ant <- 0
   atual <- 1
   cont <- 1
   Escreval(ant)
   Escreval(atual)
   enquanto cont < valor faca
            numAux <- ant + atual
            Escreval(numAux)
            ant <- atual
            atual <- numAux
            cont <- cont +1
   fimenquanto
fimalgoritmo
