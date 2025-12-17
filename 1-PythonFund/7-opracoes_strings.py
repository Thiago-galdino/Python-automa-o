gameDescription = '''
Fifa 23 é um jogo eletrônico de simulação de futebol
desenvolvido pela EA Vancouver e EA Romania e publicado pela Electronic Arts.
'''
gameName = "Fifa "
gameVersion = "23"
line = "="
# 1- operação de concatenação de strings
gameFullName = gameName + gameVersion
print(gameFullName)

# 2- operação de multiplicação de strings
line = "="
print(line * 30)  # imprime uma linha de 30 caracteres "="

# 3- procura palavra dentro de um texto
print("Fifa" in gameDescription)  # True
print("futebol" in gameDescription)   # true
print("basquete" in gameDescription)  # False