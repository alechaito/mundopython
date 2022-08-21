lista = [0, 1, 2, 3, 4, 5]

#listas iniciam na posição 0

"""
#sintaxe do slice
a[inicio:fim:passo] # por padrao o passo é 1

a[inicio:fim]  # inicio ate o final-1
a[inicio:]      # inicio ate o final
a[:final]       # do começo até o final-1
a[:]           # copia da lista
"""

print(lista[1:4]) #posicao 1 até 3
print(lista[4:]) #posicao 4 até o final
print(lista[:4]) #lista da posicao 0 até 3
print(lista[:]) # copia da lista

print(lista[-1]) # ultimo elemento
print(lista[-2:]) #ultimos 2 elementos
print(lista[:-2]) #tudo menos os ultimos 2 elementos

print(lista[::-1])
print(lista[3::-1])