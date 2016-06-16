from sklearn import tree
from funcoes_de_classificacao import *

""" TREE DECISION """
def TREE_builder(X , y , classe_alvo):
	''' gera um classificador do tipo TREE ja treinado '''
	labels_corrigidas = reorganiza_labels(classe_alvo , y)
	tree_classifier = tree.DecisionTreeClassifier()
	tree_classifier.fit(X , labels_corrigidas)
	return tree_classifier



def TREE_resultados(X_treino , y_treino , X_teste ,  y_teste):
	''' gera um vetor com os resultados de todos os classificadores do tipo TREE combinados '''
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



def TREE_probabilidades(X_treino , y_treino , X_teste ,  y_teste):
	''' gera um vetor com as probabilidades de todos os classificadores do tipo TREE combinados '''
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

	resultados_bart = tree_bart.predict_proba(X_teste)
	resultados_homer = tree_homer.predict_proba(X_teste)
	resultados_lisa = tree_lisa.predict_proba(X_teste)
	resultados_maggie = tree_maggie.predict_proba(X_teste)
	resultados_marge = tree_marge.predict_proba(X_teste)

	resultados = [resultados_bart , resultados_homer , resultados_lisa , resultados_maggie , resultados_marge]
	testes = [teste_bart , teste_homer , teste_lisa , teste_maggie , teste_marge]

	predicoes = combina_probabilidades(resultados)
	return predicoes



def TREE_votos(X_treino , y_treino , X_teste ,  y_teste):
	''' gera um vetor com as probabilidades de todos os classificadores do tipo TREE combinados '''
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

	resultados_bart = tree_bart.predict_proba(X_teste)
	resultados_homer = tree_homer.predict_proba(X_teste)
	resultados_lisa = tree_lisa.predict_proba(X_teste)
	resultados_maggie = tree_maggie.predict_proba(X_teste)
	resultados_marge = tree_marge.predict_proba(X_teste)

	resultados = [resultados_bart , resultados_homer , resultados_lisa , resultados_maggie , resultados_marge]
	testes = [teste_bart , teste_homer , teste_lisa , teste_maggie , teste_marge]

	predicoes = combina_probabilidades(resultados)
	votos = converte_probabilidades_em_labels(predicoes)
	return votos