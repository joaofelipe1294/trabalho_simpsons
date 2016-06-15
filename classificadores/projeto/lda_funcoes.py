from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from funcoes_de_classificacao import *


""" LDA """
def LDA_builder(X , y , classe_alvo):
	''' gera um objeto do tipo classificador LDA ja treinado '''
	labels_corrigidas = reorganiza_labels( classe_alvo, y)
	lda_classifier = LinearDiscriminantAnalysis()
	lda_classifier.fit(X , labels_corrigidas)
	return lda_classifier



def LDA_resultados(X_treino , y_treino , X_teste ,  y_teste):
	''' gera um vetor com os resultados de todos os classificadores LDA combinados '''
	lda_bart = LDA_builder(X_treino , y_treino , bart)
	lda_homer = LDA_builder(X_treino , y_treino , homer)
	lda_lisa = LDA_builder(X_treino , y_treino , lisa)
	lda_maggie = LDA_builder(X_treino , y_treino , maggie)
	lda_marge = LDA_builder(X_treino , y_treino , marge)

	teste_bart = reorganiza_labels(bart , y_teste)
	teste_homer = reorganiza_labels(homer , y_teste)
	teste_lisa = reorganiza_labels(lisa , y_teste)
	teste_maggie = reorganiza_labels(maggie , y_teste)
	teste_marge = reorganiza_labels(marge , y_teste)

	resultados_bart = lda_bart.predict(X_teste)
	resultados_homer = lda_homer.predict(X_teste)
	resultados_lisa = lda_lisa.predict(X_teste)
	resultados_maggie = lda_maggie.predict(X_teste)
	resultados_marge = lda_marge.predict(X_teste)	

	resultados = [resultados_bart , resultados_homer , resultados_lisa , resultados_maggie , resultados_marge]
	testes = [teste_bart , teste_homer , teste_lisa , teste_maggie , teste_marge]

	predicoes = combina_predicoes(resultados)
	return predicoes



def LDA_probabilidades(X_treino , y_treino , X_teste ,  y_teste):
	''' gera um vetor com as probabilidades referentes a cada uma das classes '''
	lda_bart = LDA_builder(X_treino , y_treino , bart)
	lda_homer = LDA_builder(X_treino , y_treino , homer)
	lda_lisa = LDA_builder(X_treino , y_treino , lisa)
	lda_maggie = LDA_builder(X_treino , y_treino , maggie)
	lda_marge = LDA_builder(X_treino , y_treino , marge)

	teste_bart = reorganiza_labels(bart , y_teste)
	teste_homer = reorganiza_labels(homer , y_teste)
	teste_lisa = reorganiza_labels(lisa , y_teste)
	teste_maggie = reorganiza_labels(maggie , y_teste)
	teste_marge = reorganiza_labels(marge , y_teste)

	resultados_bart = lda_bart.predict_proba(X_teste)
	resultados_homer = lda_homer.predict_proba(X_teste)
	resultados_lisa = lda_lisa.predict_proba(X_teste)
	resultados_maggie = lda_maggie.predict_proba(X_teste)
	resultados_marge = lda_marge.predict_proba(X_teste)	

	resultados = [resultados_bart , resultados_homer , resultados_lisa , resultados_maggie , resultados_marge]
	testes = [teste_bart , teste_homer , teste_lisa , teste_maggie , teste_marge]

	predicoes = combina_probabilidades(resultados)
	return predicoes	
