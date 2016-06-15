import os
from sklearn import preprocessing


""" CONSTANTES """
bart = 1
homer = 2
lisa = 3
maggie = 4
marge = 5   


""" FUNCOES """


def extrai_caracteristicas(diretorio , nome_arquivo):
	''' chama o executavel que extrai as caracteristicas das imagens e gera o arquivo com os vetores
	 de caracteristicas'''
	cmd = './TestCV ' + diretorio + ' ' + nome_arquivo
	result = os.system(cmd)
	if result != 0:
		print('ERRO NA EXTRACAO DE CARACTERISTICAS !!!')
		exit
	else:
		return result



def prepara_dados(nome_arquivo):
	''' le as informacoes de um arquivo , normaliza seus dados e monta uma lista com os vetores de 
	caracteristicas e outra lista com as respectivas classes '''
	arquivo = open(nome_arquivo , 'r')
	X = []
	y = []
	for linha in arquivo:
		dados = linha.split(',')
		lista = []
		contador = 0
		while contador < len(dados) - 1:
			valor = float(dados[contador])
			lista.append(valor)
			contador += 1
		X.append(lista)
		label = dados[len(dados) - 1]
		y.append(int(label))
	X_scaled = preprocessing.normalize(X, norm='l2')
	return X_scaled , y



def reorganiza_labels(classe_usada , y):
	''' reorganiza as labels para 1 (classe usada) ou 0 para as demais classes'''
	novos_dados = []
	contador = 0
	while contador < len(y):
		if y[contador] != classe_usada:
			novos_dados.append(0)
		else:
			novos_dados.append(1)
		contador += 1
	return novos_dados



def exibe_resultados(predicoes , y_teste):
	''' exibe resultados de um classificador'''
	contador = 0
	acertos = 0
	erros = 0
	rejeicoes = 0
	while contador < len(predicoes):
		if predicoes[contador] == y_teste[contador]:
			acertos += 1
		elif predicoes[contador] == 0:
			rejeicoes += 1
		elif predicoes[contador] != y_teste[contador]:
			erros += 1
		contador += 1
	print('Acertos : ' + str(acertos))
	print('Erros : ' + str(erros))
	print('Rejeicoes : ' + str(rejeicoes))
