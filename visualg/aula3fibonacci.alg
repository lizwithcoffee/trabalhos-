ggialgoritmo "aula3fibonacci"
// Fun��o :
// Autor :
// Data : 22/11/2024
// Se��o de Declara��es 
var
   ant, atual, numAux, cont, valor:inteiro

inicio
// Se��o de Comandos
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
