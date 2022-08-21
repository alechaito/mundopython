# from keys

chaves = ['a', 'b', 'c']
# creates a dictionary with keys and values
dicionario = dict.fromkeys(chaves, 1)
print(dicionario)

# --------------------------------------------

# update
materias = {'Fisica':6, 'Matemática':8}
materias_paralelas = {'Música':5}
materias.update(materias_paralelas)
print(materias)

# --------------------------------------------

# set default
pessoa = {'nome': 'Joao'}
pessoa.setdefault('salario', 1200)
print(pessoa)

# --------------------------------------------
dicionario = {'a':1, 'b':2, 'c':3}
# items
print(dicionario.items())

# values
print(dicionario.values())

# keys
print(dicionario.keys())


