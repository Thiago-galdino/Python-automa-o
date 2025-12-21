gameName = "Fifa 23"
gameDescription = '''
Fifa 23 é um jogo eletrônico de simulação de futebol
desenvolvido pela EA Vancouver e EA Romania e publicado pela Electronic Arts.
'''

# string[início:fim:] - indice começa na posição 0 | indice final e -1 

# 1 - Busque toda string a partir da primeira posição
print(gameName[0:]) # Fifa 23

# 2 - Busque toda string até a ultima posição
print(gameName[:7]) # Fifa 23

# 3 - Busque toda string da terceira até a ultima posição
print(gameName[2:]) # fa 23

'''
string[início:fim:passo] - indice começa na posição 0 | indice final e -1
passo - determina o incremento. por padrão esse numero é 1.
'''
# 4 - Busque toda string  de 2 em 2 caracteres
print(gameName[::2]) # Ff 3

# 5 - Busque toda string nos indeces ímpares
print(gameName[1::2]) # ia2

# 6 - Inverter uma string de tras para frente
print(gameName[::-1]) # 32 afiF