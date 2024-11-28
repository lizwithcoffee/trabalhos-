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
    