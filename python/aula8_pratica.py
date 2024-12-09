# Bhaskara

a = b = c = xm = xn  = d = r = dn = 0

a = float(input("Digite valor de a: "))
b = float(input("Digite valor de b: "))
c = float(input("Digite valor de c: "))

d = ((b*b)-(4*a*c))
print("Delta: ",d)

if d<0:
    dn = -(d)
    r = d**(1/2)
    print("Raiz de Delta: ", r)
    xm = ((-b + (r)) / (2*a))
    print("O valor de X1 é: ", xm, "!")
    xn = ((b - (r)) / (2*a))
    print("O valor de X'' é: ", xn, "!")

else:
     r = d** (1/2)
     print("Raiz de Delta:",r)
     xm = ((-b + (r)) / (2*a))
     print("O valor de X' é: ", xm)
     xn = ((-b - (r) ) / (2*a))
     print("O valor de X'' é: ",xn)

# Fatorial

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
