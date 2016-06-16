from sklearn.neural_network import MLPClassifier
from funcoes_de_classificacao import *


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



def MLP_probabilidades(X_treino , y_treino , X_teste ,  y_teste):
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

	resultados_bart = mlp_bart.predict_proba(X_teste)
	resultados_homer = mlp_homer.predict_proba(X_teste)
	resultados_lisa = mlp_lisa.predict_proba(X_teste)
	resultados_maggie = mlp_maggie.predict_proba(X_teste)
	resultados_marge = mlp_marge.predict_proba(X_teste)

	resultados = [resultados_bart , resultados_homer , resultados_lisa , resultados_maggie , resultados_marge]
	testes = [teste_bart , teste_homer , teste_lisa , teste_maggie , teste_marge]

	predicoes = combina_probabilidades(resultados)
	return predicoes
