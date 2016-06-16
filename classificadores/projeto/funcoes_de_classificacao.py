from functions import *
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier



""" CONSTANTES """
bart = 1
homer = 2
lisa = 3
maggie = 4
marge = 5   


""" FUNCOES """


def combina_predicoes(resultados):
	''' combina as saidas dos classificadores em um unico vetor com os resultados '''
	lista_saida = []
	cont_resultados = 0
	iteracoes = len(resultados[0])
	while cont_resultados < iteracoes:
		lista = []
		cont_posicao = 0
		iteracoes_posicao = len(resultados)
		while cont_posicao < iteracoes_posicao:
			lista.append(resultados[cont_posicao][cont_resultados])
			cont_posicao += 1
		lista_saida.append(lista)
		cont_resultados += 1

	predicoes = []
	for result in lista_saida:
		aparicoes = 0
		contador = 0
		index = 0
		while contador < len(result):
			if result[contador] == 1:
				aparicoes += 1
				index = contador
			contador += 1
		if aparicoes == 1:
			predicoes.append(index + 1)
		elif (aparicoes > 1) or (aparicoes == 0):
			predicoes.append(0)
	return predicoes



def combina_probabilidades(resultados):
	''' combina as probabilidades de cada um dos classificadores em um vetor com as 
	probabilidades de cada  uma das cinco classes possiveis'''
	lista_probabilidades = []
	iteracoes = len(resultados[0])
	iteracoes_classe = len(resultados)
	contador = 0
	while contador < iteracoes:
		lista = []
		contador_classe = 0
		while contador_classe < iteracoes_classe:
			lista.append(resultados[contador_classe][contador][1])
			contador_classe += 1
		contador += 1
		lista_probabilidades.append(lista)
	return lista_probabilidades



def converte_probabilidades_em_labels(probabilidades):
	''' escolhe a label de acordo com a mair probabilidade '''
	labels = []
	contador_prob = 0
	iteracoes_prob = len(probabilidades)
	while contador_prob < iteracoes_prob:
		maio_prob = probabilidades[contador_prob][0]
		index_maior = 0
		contador_label = 1
		iteracoes_label = len(probabilidades[contador_prob])
		while contador_label < iteracoes_label:
			if probabilidades[contador_prob][contador_label] > maio_prob:
				maio_prob = probabilidades[contador_prob][contador_label]
				index_maior = contador_label
			contador_label += 1
		contador_prob += 1
		labels.append(index_maior + 1)
	return labels



def prepara_classificadores(argv):
	''' monta uma lista ordenada com os classificadores informados '''
	classificadores = []
	contador = 3
	while contador < len(argv) - 1:
		classificadores.append(argv[contador])
		contador += 1
	classificadores.sort()
	return classificadores



def calcula_votos(votos):
	classes = []
	contador_votos = 0
	iteracoes_votos = len(votos[0])
	while contador_votos < iteracoes_votos:
		contador = 0
		iteracoes = len(votos)
		bart_votos = 0
		homer_votos = 0
		lisa_votos = 0
		maggie_votos = 0
		marge_votos = 0
		while contador < iteracoes:
			if votos[contador][contador_votos] == bart:
				bart_votos += 1

			elif votos[contador][contador_votos] == homer:
				homer_votos += 1

			elif votos[contador][contador_votos] == lisa:
				lisa_votos += 1

			elif votos[contador][contador_votos] == maggie:
				maggie_votos += 1

			elif votos[contador][contador_votos] == marge:
				marge_votos += 1			

			contador += 1


		if bart_votos > homer_votos and bart_votos > lisa_votos and bart_votos > maggie_votos and bart_votos > marge_votos:
			classes.append(bart)

		elif homer_votos > bart_votos and homer_votos > lisa_votos and homer_votos > maggie_votos and homer_votos > marge_votos:
			classes.append(homer)

		elif lisa_votos > bart_votos and lisa_votos > homer_votos and lisa_votos > maggie_votos and lisa_votos > marge_votos:
			classes.append(lisa)

		elif maggie_votos > bart_votos and maggie_votos > homer_votos and maggie_votos > lisa_votos and maggie_votos > marge_votos:
			classes.append(maggie)

		elif marge_votos > bart_votos and marge_votos > homer_votos and marge_votos > lisa_votos and marge_votos > lisa_votos:
			classes.append(marge)

		contador_votos += 1
	return classes


