algoritmo "aula3parcelas"
// Função :
// Autor :
// Data : 22/11/2024
// Seção de Declarações 
var
   valorEmp, juros, parcelas, rJuros, resposta: Real

inicio
// Seção de Comandos
   Escreval ("Quanto vou pagar de empréstimo? R$ ")
   Leia (valorEmp)
   Escreval ()
   Escreval ("Qual o valor dos juros cobrados pelo banco em % ? ")
   Leia(juros)
   Escreval ()
   Escreval ("Quantas parcelas quero dividir para pagar? ")
   Leia (parcelas)
   rJuros <- ((valorEmp * juros) /100)
   Escreval ()
   Escreval ()
   Escreval ("O valor dos meus juros será de R$ ",rJuros:5:2)
   resposta <- (rJuros + valorEmp) / parcelas
   Escreval ()
   Escreval ()
   Escreval ()
   Escreval ()
   Escreval ("O valor das ", parcelas, " parcelas que terei que pagar é de R$ ", resposta:5:2)
fimalgoritmo
