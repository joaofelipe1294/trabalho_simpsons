from sys import argv
from functions import *
from funcoes_de_classificacao import *
from lda_funcoes import *
from svm_funcoes import *
from knn_funcoes import *
from tree_funcoes import *
from mlp_funcoes import *
from fusao_classificadores import *

""" CONSTANTES """
bart = 1
homer = 2
lisa = 3
maggie = 4
marge = 5   
""""""""""""""""""


""" prepara dados """
argc = len(argv)
dir_treino = argv[1]
dir_validacao = argv[2]
X_treino , y_treino = prepara_dados('treino.txt')
X_teste , y_teste = prepara_dados('validacao.txt')
""""""""""""""""""""

if argc == 4:                         
	''' executa apenas um classificador '''
	nome_classificador = argv[3]
	labels = None
	classificador = None
	if nome_classificador == 'knn' or nome_classificador == 'KNN':
		classificador = KNN_probabilidades(X_treino , y_treino , X_teste , y_teste , 11)

	elif nome_classificador == 'lda' or nome_classificador == 'LDA':
		classificador =  LDA_probabilidades(X_treino , y_treino , X_teste ,  y_teste)

	elif nome_classificador == 'svm' or nome_classificador == 'SVM':
		classificador = SVM_probabilidades(X_treino , y_treino , X_teste , y_teste)

	elif nome_classificador == 'tree' or nome_classificador == 'TREE':
		classificador = TREE_probabilidades(X_treino , y_treino , X_teste , y_teste)

	elif nome_classificador == 'mlp' or nome_classificador == 'MLP':
		classificador = MLP_probabilidades(X_treino , y_treino , X_teste , y_teste)

	else:
		print('Nenhum classificador foi selecionado')
	
	labels = converte_probabilidades_em_labels(classificador)
	gera_resultados(labels , y_teste)

elif argc > 4 and argc < 10:
	metodo = argv[len(argv) - 1]
	classificadores = prepara_classificadores(argv)
	if metodo == 'voto' or metodo == 'VOTO':
		votos = []		
		contador = 0
		while contador < len(classificadores):
			if classificadores[contador] == 'knn' or classificadores[contador] == 'KNN':
				knn_votos = KNN_votos(X_treino , y_treino , X_teste , y_teste , 5)
				votos.append(knn_votos)

			elif classificadores[contador] == 'lda' or classificadores[contador] == 'LDA':
				lda_votos = LDA_votos(X_treino , y_treino , X_teste , y_teste)
				votos.append(lda_votos)

			elif classificadores[contador] == 'svm' or classificadores[contador] == 'SVM':
				svm_votos = SVM_votos(X_treino , y_treino , X_teste , y_teste)
				votos.append(svm_votos)

			elif classificadores[contador] == 'tree' or classificadores[contador] == 'TREE':
				tree_votos = TREE_votos(X_treino , y_treino , X_teste , y_teste)
				votos.append(tree_votos)

			elif classificadores[contador] == 'mlp' or classificadores[contador] == 'MLP':
				mlp_votos = MLP_votos(X_treino , y_treino , X_teste , y_teste)
				votos.append(mlp_votos)

			contador += 1
		labels = calcula_votos(votos)
		gera_resultados(labels , y_teste)

	elif metodo == 'soma' or metodo == 'SOMA':
		probabilidades = []		
		contador = 0
		while contador < len(classificadores):
			if classificadores[contador] == 'knn' or classificadores[contador] == 'KNN':
				knn = KNN_probabilidades(X_treino , y_treino , X_teste , y_teste , 5)
				probabilidades.append(knn)

			elif classificadores[contador] == 'lda' or classificadores[contador] == 'LDA':
				lda = LDA_probabilidades(X_treino , y_treino , X_teste , y_teste)
				probabilidades.append(lda)

			elif classificadores[contador] == 'svm' or classificadores[contador] == 'SVM':
				svm = SVM_probabilidades(X_treino , y_treino , X_teste , y_teste)
				probabilidades.append(svm)

			elif classificadores[contador] == 'tree' or classificadores[contador] == 'TREE':
				tree = TREE_probabilidades(X_treino , y_treino , X_teste , y_teste)
				probabilidades.append(tree)

			elif classificadores[contador] == 'mlp' or classificadores[contador] == 'MLP':
				mlp = MLP_probabilidades(X_treino , y_treino , X_teste , y_teste)
				probabilidades.append(mlp)

			contador += 1
		labels = soma(probabilidades)
		#print(labels)
		gera_resultados(labels , y_teste)		















'''

""" LDA """
print("============ LDA  ============")
lda_predicoes =  LDA_resultados(X_treino , y_treino , X_teste ,  y_teste)
exibe_resultados(lda_predicoes , y_teste)

print("========== LDA PROB ==========")
lda_probabilidades =  LDA_probabilidades(X_treino , y_treino , X_teste ,  y_teste)
labels_prob = converte_probabilidades_em_labels(lda_probabilidades)
exibe_resultados(labels_prob , y_teste)


""" SVM """
print("============ SVM ============")
svm_predicoes = SVM_resultados(X_treino , y_treino , X_teste , y_teste)
exibe_resultados(svm_predicoes , y_teste)

print("========== SVM PROB ==========")
svm_prob = SVM_probabilidades(X_treino , y_treino , X_teste , y_teste)
labels_prob = converte_probabilidades_em_labels(svm_prob)
exibe_resultados(labels_prob , y_teste)


""" KNN """
print("============ KNN ============")
knn_predicoes = KNN_resultados(X_treino , y_treino , X_teste , y_teste , 5)
exibe_resultados(knn_predicoes , y_teste)

print("========== KNN PROB ==========")
knn_prob = KNN_probabilidades(X_treino , y_treino , X_teste , y_teste , 5)
labels_prob = converte_probabilidades_em_labels(knn_prob)
exibe_resultados(labels_prob , y_teste)


""" TREE """
print("============ TREE ============")
tree_predicoes = TREE_resultados(X_treino , y_treino , X_teste , y_teste)
exibe_resultados(tree_predicoes , y_teste)

print("========== TREE PROB ==========")
tree_prob = TREE_probabilidades(X_treino , y_treino , X_teste , y_teste)
labels_prob = converte_probabilidades_em_labels(tree_prob)
exibe_resultados(labels_prob , y_teste)



""" MLP """
print("============ MLP ============")
mlp_predicoes = MLP_resultados(X_treino , y_treino , X_teste , y_teste)
exibe_resultados(mlp_predicoes , y_teste)

print("========== MLP PROB ==========")
mlp_prob = MLP_probabilidades(X_treino , y_treino , X_teste , y_teste)
labels_prob = converte_probabilidades_em_labels(mlp_prob)
exibe_resultados(labels_prob , y_teste)
'''