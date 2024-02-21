qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor:"))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1
# Entrada de Valores
    valor = float(input("Digite um valor:"))

#caso digite um valot negativo o laço encerra
media = soma / qtd 
print("\n Total da Soma:",soma)
print("\n Quantidades de Valores Digitados:",qtd)
print("\n Média dos Valores:", media)