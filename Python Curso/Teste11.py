notaA=float(input("Informe a Primeira Nota:"))
notaB=float(input("Informe a Segunda Nota:"))

#calcular media
mediafinal = (notaA + notaB) / 2

#verificação
if mediafinal >=7.0:
    print("A média: %.1f - Aprovado "% mediafinal)
else:
    print("A Média: %.1f - Reprovado"% mediafinal)
