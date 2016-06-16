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



def gera_resultados(labels_geradas , labels_corretas):
	lista_bart = [0 , 0 , 0 , 0 , 0]
	lista_homer = [0 , 0 , 0 , 0 , 0]
	lista_lisa = [0 , 0 , 0 , 0 , 0]
	lista_maggie = [0 , 0 , 0 , 0 , 0]
	lista_marge = [0 , 0 , 0 , 0 , 0]
	bart_posicao = 0
	homer_posicao = 1
	lisa_posicao = 2
	maggie_posicao = 3
	marge_posicao = 4
	contador = 0
	classificados_corretos = 0
	iteracoes = len(labels_geradas)
	while contador < iteracoes:
		if labels_corretas[contador] == bart:

			if labels_geradas[contador] == bart:
				lista_bart[bart_posicao] += 1
				classificados_corretos += 1

			elif labels_geradas[contador] == homer:
				lista_bart[homer_posicao] += 1

			elif labels_geradas[contador] == lisa:
				lista_bart[lisa_posicao] += 1

			elif labels_geradas[contador] == maggie:
				lista_bart[maggie_posicao] += 1

			elif labels_geradas[contador] == marge:
				lista_bart[marge_posicao] += 1

		elif labels_corretas[contador] == homer:

			if labels_geradas[contador] == bart:
				lista_homer[bart_posicao] += 1

			elif labels_geradas[contador] == homer:
				lista_homer[homer_posicao] += 1
				classificados_corretos += 1

			elif labels_geradas[contador] == lisa:
				lista_homer[lisa_posicao] += 1

			elif labels_geradas[contador] == maggie:
				lista_homer[maggie_posicao] += 1

			elif labels_geradas[contador] == marge:
				lista_homer[marge_posicao] += 1

		elif labels_corretas[contador] == lisa:

			if labels_geradas[contador] == bart:
					lista_lisa[bart_posicao] += 1

			elif labels_geradas[contador] == homer:
				lista_lisa[homer_posicao] += 1

			elif labels_geradas[contador] == lisa:
				lista_lisa[lisa_posicao] += 1
				classificados_corretos += 1

			elif labels_geradas[contador] == maggie:
				lista_lisa[maggie_posicao] += 1

			elif labels_geradas[contador] == marge:
				lista_lisa[marge_posicao] += 1

		elif labels_corretas[contador] == maggie:

			if labels_geradas[contador] == bart:
				lista_maggie[bart_posicao] += 1

			elif labels_geradas[contador] == homer:
				lista_maggie[homer_posicao] += 1

			elif labels_geradas[contador] == lisa:
				lista_maggie[lisa_posicao] += 1

			elif labels_geradas[contador] == maggie:
				lista_maggie[maggie_posicao] += 1
				classificados_corretos += 1

			elif labels_geradas[contador] == marge:
				lista_maggie[marge_posicao] += 1

		elif labels_corretas[contador] == marge:

			if labels_geradas[contador] == bart:
				lista_marge[bart_posicao] += 1

			elif labels_geradas[contador] == homer:
				lista_marge[homer_posicao] += 1

			elif labels_geradas[contador] == lisa:
				lista_marge[lisa_posicao] += 1

			elif labels_geradas[contador] == maggie:
				lista_marge[maggie_posicao] += 1

			elif labels_geradas[contador] == marge:
				lista_marge[marge_posicao] += 1
				classificados_corretos += 1

		contador += 1
	print('+%-10s+%-10s+%-10s+%-10s+%-10s+%-10s+' % ('-' * 10 , '-' * 10 , '-' * 10 , '-' * 10 , '-' * 10 , '-' * 10))
	print('|%-10s|%-10s|%-10s|%-10s|%-10s|%-10s|' % (' ' * 10 , 'BART' , 'HOMER' , 'LISA' , 'MAGGIE' , 'MARGE'))
	print('+%-10s+%-10s+%-10s+%-10s+%-10s+%-10s+' % ('-' * 10 , '-' * 10 , '-' * 10 , '-' * 10 , '-' * 10 , '-' * 10))
	print('|%-10s|%-10s|%-10s|%-10s|%-10s|%-10s|' % ('BART' ,(' ' * 4 ) + str(lista_bart[0]) , (' ' * 4 ) + str(lista_bart[1]) , (' ' * 4 ) + str(lista_bart[2]) , (' ' * 4 ) + str(lista_bart[3]) , (' ' * 4 ) + str(lista_bart[4])))
	print('+%-10s+%-10s+%-10s+%-10s+%-10s+%-10s+' % ('-' * 10 , '-' * 10 , '-' * 10 , '-' * 10 , '-' * 10 , '-' * 10))
	print('|%-10s|%-10s|%-10s|%-10s|%-10s|%-10s|' % ('HOMER' ,(' ' * 4 ) + str(lista_homer[0]) , (' ' * 4 ) + str(lista_homer[1]) , (' ' * 4 ) + str(lista_homer[2]) , (' ' * 4 ) + str(lista_homer[3]) , (' ' * 4 ) + str(lista_homer[4])))
	print('+%-10s+%-10s+%-10s+%-10s+%-10s+%-10s+' % ('-' * 10 , '-' * 10 , '-' * 10 , '-' * 10 , '-' * 10 , '-' * 10))
	print('|%-10s|%-10s|%-10s|%-10s|%-10s|%-10s|' % ('LISA' ,(' ' * 4 ) + str(lista_lisa[0]) , (' ' * 4 ) + str(lista_lisa[1]) , (' ' * 4 ) + str(lista_lisa[2]) , (' ' * 4 ) + str(lista_lisa[3]) , (' ' * 4 ) + str(lista_lisa[4])))
	print('+%-10s+%-10s+%-10s+%-10s+%-10s+%-10s+' % ('-' * 10 , '-' * 10 , '-' * 10 , '-' * 10 , '-' * 10 , '-' * 10))
	print('|%-10s|%-10s|%-10s|%-10s|%-10s|%-10s|' % ('MAGGIE' ,(' ' * 4 ) + str(lista_maggie[0]) , (' ' * 4 ) + str(lista_maggie[1]) , (' ' * 4 ) + str(lista_maggie[2]) , (' ' * 4 ) + str(lista_maggie[3]) , (' ' * 4 ) + str(lista_maggie[4])))
	print('+%-10s+%-10s+%-10s+%-10s+%-10s+%-10s+' % ('-' * 10 , '-' * 10 , '-' * 10 , '-' * 10 , '-' * 10 , '-' * 10))
	print('|%-10s|%-10s|%-10s|%-10s|%-10s|%-10s|' % ('MARGE' ,(' ' * 4 ) + str(lista_marge[0]) , (' ' * 4 ) + str(lista_marge[1]) , (' ' * 4 ) + str(lista_marge[2]) , (' ' * 4 ) + str(lista_marge[3]) , (' ' * 4 ) + str(lista_marge[4])))
	print('+%-10s+%-10s+%-10s+%-10s+%-10s+%-10s+' % ('-' * 10 , '-' * 10 , '-' * 10 , '-' * 10 , '-' * 10 , '-' * 10))
	#print(lista_bart)
	#print(lista_homer)
	#print(lista_lisa)
	#print(lista_maggie)
	#print(lista_marge)
	print('Taxa de reconhecimento : ' + str(classificados_corretos / len(labels_corretas)))




















