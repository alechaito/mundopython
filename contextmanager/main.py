#modo antigo
#with ja e preparado pra abrir e fechar
#eduardo mendes um salve
# isso saiu na PEP 343 (Python Echancement Proposals)

#modo antigo
try:
    file = open('test.txt', 'w')
    file.write('Ola Mundo')
finally:
    file.close()

#serve pra tudo que voce precisa abrir e fechar
with open('test.txt', 'w') as file:
    file.write("Ola mundo")


class Test:
    def __init__(self) -> None:
        pass

    def __enter__(self):
        print("Entrei no contexto")
    
    def __exit__(self, type, value, traceback):
        print("Sai do contexto")
    

with Test() as test:
    print("Executando contexto")




