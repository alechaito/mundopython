letras = 'aabbbccde'

letras_unicas = list(set(letras))

resultado = []
for letra in letras_unicas:
    resultado.append( (letra, letras.count(letra)) )

print(resultado)

# ordeno por ordem alfabética
resultado = sorted(resultado, key=lambda item: item[0])
print(resultado)

# ordeno pelo numero de ocorrencias na ordem inversa do maior para o menor
resultado = sorted(resultado, key=lambda item: item[1], reverse=True)
print(resultado)

# imprimir os 3 resultados mais comuns
for i in range(3):
    print(f"{resultado[i][0]} {resultado[i][1]}")



