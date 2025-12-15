name = input('Digite o nome do jogo:\n')
yearLaunch = int(input('Digite o ano de lançamento do jogo:\n'))
gamePrice = float(input('Digite o preço do jogo:\n'))
planInclude = (input('Está incluso no serviço mensal?\n'))

# 1º alternariva 

print('#####Dados do jogo #######')
print('===========================')
# print('Nome do jogo:', name)
# print('Ano do jogo:', yearLaunch)
# print('Preço do Jogo:', gamePrice)
# print('Está incluido no plano?', planInclude)

# 2º alternativa
# print("Nome do Jogo:", name, "\n Ano de Lançamento:", yearLaunch, "\n Preço do Jogo:", gamePrice, "\n Incluido no Plano?:", planInclude)

# 3º alternativa
print(f'Nome do Jogo: {name} \n Ano de Lançamento: {yearLaunch} \n Preço do Jogo: {gamePrice} \n Incluido no Plano?: {planInclude}')
