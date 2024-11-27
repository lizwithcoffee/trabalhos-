vendas = 1500
meta = 1800

# # >    maior que
# # <    menor que
# # >=   maior ou igual a
# # <=   menor ou igual a
# # ==   igual a
# # !=   diferente

if vendas >= meta:
    print("Vendedor ganhou bonus")
    print("Bateu a meta de vendas")
    bonus = 0.1 * vendas
    print("Bonus do vendedor:", bonus)
else:
    print("Vendedor não ganhou bonus")
    print("Não bateu a meta de vendas")

print("Acabou o programa")

# Segundo cenário

vendas = 1500
metal = 1300 # Ganha 10%
meta = 2000 # Ganha 13%

if vendas >= 2000:
    bonus = 0.13 * vendas
else:
    if vendas >= 1300:
        bonus = 0.1 * vendas
    else:
        bonus = 0

print("Bonus:", bonus)

# Terceiro cenário

vendas = 2500
vendas_empresa = 10000
meta_empresa = 20000
meta1 = 1300 # Ganha 10%
meta = 2000 # Ganha 13%

if vendas >= 2000 and vendas_empresa >= meta_empresa:
    bonus = 0.13 * vendas
elif vendas >= 1300 and vendas_empresa >= meta_empresa:
    bonus = 0.1 * vendas
else:
    bonus = 0

print("Bonus: ", bonus)

lista_produtos = ["airpod", "ipad", "iphone", "macbook"]
produto_procurado = input("Procure um produto: ")
produto_procurado = produto_procurado.lower()

if produto_procurado in lista_produtos:
    print("Produto em estoque.")
else:
    print("Não temos esse produto em estoque.")
