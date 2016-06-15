from sklearn.neighbors import KNeighborsClassifier
from functions import *
from funcoes_de_classificacao import *

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



def KNN_probabilidades(X_treino , y_treino , X_teste ,  y_teste , k):
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

	resultados_bart = knn_bart.predict_proba(X_teste)
	resultados_homer = knn_homer.predict_proba(X_teste)
	resultados_lisa = knn_lisa.predict_proba(X_teste)
	resultados_maggie = knn_maggie.predict_proba(X_teste)
	resultados_marge = knn_marge.predict_proba(X_teste)

	resultados = [resultados_bart , resultados_homer , resultados_lisa , resultados_maggie , resultados_marge]
	testes = [teste_bart , teste_homer , teste_lisa , teste_maggie , teste_marge]

	predicoes = combina_probabilidades(resultados)
	return predicoes
