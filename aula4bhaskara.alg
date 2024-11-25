algoritmo "aula4bhaskara"
// Função :
// Autor :
// Data : 25/11/2024
// Seção de Declarações 
var
   a, b, c, xm, xn, d, r, dn: Real

inicio
// Seção de Comandos
   Escreval("Digite o valor de a:")
   Leia(a)
   Escreval
   Escreval
   Escreval("Digite o valor de b:")
   Leia(b)
   Escreval("Digite o valor de c:")
   Leia(c)
   Escreval
   Escreval
   d<-((b*b)-(4*a*c))
   Escreval("Delta: ",d)
   se d<0 entao
      dn <- -(d)
      r <- RaizQ(d)
      Escreval("Raiz de Delta: ", r)
      xm <- ((-b + (r)) /(2*a))
      Escreval("O valor de X1 é: " ,xm "!")
      Escreval
      Escreval
      xn <- ((b - (r)) / (2*a))
      Escreval("O valor de X'' é: ",xn, "!")
      senao
      r <- RaizQ(d)
      Escreval("Raiz de Delta:",r)
      xm <- ((-b + (r)) / (2*a))
      Escreval ("O valor de X' é: ", xm)
      Escreval
      Escreval
      xn <- ((-b - (r) ) / (2*a))
      Escreval("O valor de X'' é: ",xn)

fimse
fimalgoritmo
