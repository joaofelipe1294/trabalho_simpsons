from functions import *
from sklearn import preprocessing
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn import tree



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



""" SVM """
def SVM_builder(X , y , classe_alvo):
	''' gera um classificador do tipo SVM ja treinado '''
	labels_corrigidas = reorganiza_labels(classe_alvo , y)
	svm_classifier = svm.SVC()
	svm_classifier.fit(X , labels_corrigidas)
	return svm_classifier



def SVM_resultados(X_treino , y_treino , X_teste ,  y_teste):
	''' gera um vetor com os resultados de todos os classificadores SVM combinados '''
	svm_bart = SVM_builder(X_treino , y_treino , bart)
	svm_homer = SVM_builder(X_treino , y_treino , homer)
	svm_lisa = SVM_builder(X_treino , y_treino , lisa)
	svm_maggie = SVM_builder(X_treino , y_treino , maggie)
	svm_marge = SVM_builder(X_treino , y_treino , marge)

	teste_bart = reorganiza_labels(bart , y_teste)
	teste_homer = reorganiza_labels(homer , y_teste)
	teste_lisa = reorganiza_labels(lisa , y_teste)
	teste_maggie = reorganiza_labels(maggie , y_teste)
	teste_marge = reorganiza_labels(marge , y_teste)

	resultados_bart = svm_bart.predict(X_teste)
	resultados_homer = svm_homer.predict(X_teste)
	resultados_lisa = svm_lisa.predict(X_teste)
	resultados_maggie = svm_maggie.predict(X_teste)
	resultados_marge = svm_marge.predict(X_teste)

	resultados = [resultados_bart , resultados_homer , resultados_lisa , resultados_maggie , resultados_marge]
	testes = [teste_bart , teste_homer , teste_lisa , teste_maggie , teste_marge]

	predicoes = combina_predicoes(resultados)
	return predicoes	



""" KNN """
def KNN_builder(X , y , classe_alvo , k):
	''' gera um classificador do tipo KNN ja treinado '''
	labels_corrigidas = reorganiza_labels(classe_alvo , y)
	knn_classifier = KNeighborsClassifier(n_neighbors=k)
	knn_classifier.fit(X , labels_corrigidas)
	return knn_classifier



def KNN_resultados(X_treino , y_treino , X_teste ,  y_teste , k):
	''' gera um vetor com os resultados de todos os classificadores KNN combinados '''
	knn_bart = KNN_builder(X_treino , y_treino , bart , k)
	knn_homer = KNN_builder(X_treino , y_treino , homer , k)
	knn_lisa = KNN_builder(X_treino , y_treino , lisa , k)
	knn_maggie = KNN_builder(X_treino , y_treino , maggie , k)
	knn_marge = KNN_builder(X_treino , y_treino , marge , k)

	teste_bart = reorganiza_labels(bart , y_teste)
	teste_homer = reorganiza_labels(homer , y_teste)
	teste_lisa = reorganiza_labels(lisa , y_teste)
	teste_maggie = reorganiza_labels(maggie , y_teste)
	teste_marge = reorganiza_labels(marge , y_teste)

	resultados_bart = knn_bart.predict(X_teste)
	resultados_homer = knn_homer.predict(X_teste)
	resultados_lisa = knn_lisa.predict(X_teste)
	resultados_maggie = knn_maggie.predict(X_teste)
	resultados_marge = knn_marge.predict(X_teste)

	resultados = [resultados_bart , resultados_homer , resultados_lisa , resultados_maggie , resultados_marge]
	testes = [teste_bart , teste_homer , teste_lisa , teste_maggie , teste_marge]

	predicoes = combina_predicoes(resultados)
	return predicoes


""" MLP """
def MLP_builder(X , y , classe_alvo):
	''' gera um classificador do tipo MLP ja treinado '''
	labels_corrigidas = reorganiza_labels(classe_alvo , y)
	mlp_classifier = MLPClassifier(max_iter=1000)
	mlp_classifier.fit(X , labels_corrigidas)
	return mlp_classifier



def MLP_resultados(X_treino , y_treino , X_teste ,  y_teste):
	''' gera um vetor com os resultados de todos os classificadores MLP combinados '''
	mlp_bart = MLP_builder(X_treino , y_treino , bart)
	mlp_homer = MLP_builder(X_treino , y_treino , homer)
	mlp_lisa = MLP_builder(X_treino , y_treino , lisa)
	mlp_maggie = MLP_builder(X_treino , y_treino , maggie)
	mlp_marge = MLP_builder(X_treino , y_treino , marge)

	teste_bart = reorganiza_labels(bart , y_teste)
	teste_homer = reorganiza_labels(homer , y_teste)
	teste_lisa = reorganiza_labels(lisa , y_teste)
	teste_maggie = reorganiza_labels(maggie , y_teste)
	teste_marge = reorganiza_labels(marge , y_teste)

	resultados_bart = mlp_bart.predict(X_teste)
	resultados_homer = mlp_homer.predict(X_teste)
	resultados_lisa = mlp_lisa.predict(X_teste)
	resultados_maggie = mlp_maggie.predict(X_teste)
	resultados_marge = mlp_marge.predict(X_teste)

	resultados = [resultados_bart , resultados_homer , resultados_lisa , resultados_maggie , resultados_marge]
	testes = [teste_bart , teste_homer , teste_lisa , teste_maggie , teste_marge]

	predicoes = combina_predicoes(resultados)
	return predicoes



""" MULTINOMIAL BAYES """
def TREE_builder(X , y , classe_alvo):
	''' gera um classificador do tipo MULTINOMIAL BAYES ja treinado '''
	labels_corrigidas = reorganiza_labels(classe_alvo , y)
	tree_classifier = tree.DecisionTreeClassifier() #MultinomialNB()
	tree_classifier.fit(X , labels_corrigidas)
	return tree_classifier



def TREE_resultados(X_treino , y_treino , X_teste ,  y_teste):
	''' gera um vetor com os resultados de todos os classificadores BAbayes combinados '''
	tree_bart = TREE_builder(X_treino , y_treino , bart)
	tree_homer = TREE_builder(X_treino , y_treino , homer)
	tree_lisa = TREE_builder(X_treino , y_treino , lisa)
	tree_maggie = TREE_builder(X_treino , y_treino , maggie)
	tree_marge = TREE_builder(X_treino , y_treino , marge)

	teste_bart = reorganiza_labels(bart , y_teste)
	teste_homer = reorganiza_labels(homer , y_teste)
	teste_lisa = reorganiza_labels(lisa , y_teste)
	teste_maggie = reorganiza_labels(maggie , y_teste)
	teste_marge = reorganiza_labels(marge , y_teste)

	resultados_bart = tree_bart.predict(X_teste)
	resultados_homer = tree_homer.predict(X_teste)
	resultados_lisa = tree_lisa.predict(X_teste)
	resultados_maggie = tree_maggie.predict(X_teste)
	resultados_marge = tree_marge.predict(X_teste)

	resultados = [resultados_bart , resultados_homer , resultados_lisa , resultados_maggie , resultados_marge]
	testes = [teste_bart , teste_homer , teste_lisa , teste_maggie , teste_marge]

	predicoes = combina_predicoes(resultados)
	return predicoes

