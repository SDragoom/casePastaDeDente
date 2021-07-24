from flask import Flask
import requests
import json

print('####################################################################################')
print('################ QUANTIDADE DE PASTAS VENDIDAS ATUALMENTE NO BRASIL ################')
print('####################################################################################')
print()
print('####################################################################################')
'''requestpop = requests.get('https://servicodados.ibge.gov.br/api/v1/paises/BR/indicadores/77849')

requestpy = json.loads(requestpop.content)
print('teste = ' , requestpy)'''

request = requests.get('https://servicodados.ibge.gov.br/api/v1/projecoes/populacao')
requestpy = json.loads(request.content)
horario = requestpy['horario']
show = requestpy['projecao']
showpop = float(show['populacao'])
qtd_porEscova = 0.3
refeicoes = 3
qtd_diariaPessoa = float(qtd_porEscova * refeicoes)
qtd_anualPessoa = float(365* qtd_diariaPessoa)
qtd_pastaDentG = int(qtd_anualPessoa * showpop)
qtd_pastaVend = int(qtd_pastaDentG / 90)


print ('### horario da informação: ', horario , '                                 ###')
print ('### quantidade da populacao: ', showpop , '                                       ###') 
print ('### Consumo aproximado de pasta de dente(Diaria - Adulto): ' , qtd_diariaPessoa , '  ###')
print ('### Consumo aproximado de pasta de dente(Ano por pessoa): ' , qtd_anualPessoa , '   ###')
print ('### Consumo aproximado de pasta de dente(Ano em Gramas): ' , qtd_pastaDentG , '           ###')
print ('### Consumo aproximado de pasta de dente(Ano, tubos 90g Pais): ', qtd_pastaVend , '       ###')
print ('####################################################################################')
print ()