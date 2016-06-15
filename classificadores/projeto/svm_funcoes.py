from sklearn import svm
from funcoes_de_classificacao import *


""" SVM """
def SVM_builder(X , y , classe_alvo):
	''' gera um classificador do tipo SVM ja treinado '''
	labels_corrigidas = reorganiza_labels(classe_alvo , y)
	svm_classifier = svm.SVC()
	svm_classifier.fit(X , labels_corrigidas)
	return svm_classifier



def SVM_prob_builder(X , y , classe_alvo):
	''' gera um classificador do tipo SVM para estimar as probabilidades das classes ja treinado '''
	labels_corrigidas = reorganiza_labels(classe_alvo , y)
	svm_classifier = svm.SVC(probability=True)
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



def SVM_probabilidades(X_treino , y_treino , X_teste ,  y_teste):
	''' gera um vetor com os resultados de todos os classificadores SVM combinados '''
	svm_bart = SVM_prob_builder(X_treino , y_treino , bart)
	svm_homer = SVM_prob_builder(X_treino , y_treino , homer)
	svm_lisa = SVM_prob_builder(X_treino , y_treino , lisa)
	svm_maggie = SVM_prob_builder(X_treino , y_treino , maggie)
	svm_marge = SVM_prob_builder(X_treino , y_treino , marge)

	teste_bart = reorganiza_labels(bart , y_teste)
	teste_homer = reorganiza_labels(homer , y_teste)
	teste_lisa = reorganiza_labels(lisa , y_teste)
	teste_maggie = reorganiza_labels(maggie , y_teste)
	teste_marge = reorganiza_labels(marge , y_teste)

	resultados_bart = svm_bart.predict_proba(X_teste)
	resultados_homer = svm_homer.predict_proba(X_teste)
	resultados_lisa = svm_lisa.predict_proba(X_teste)
	resultados_maggie = svm_maggie.predict_proba(X_teste)
	resultados_marge = svm_marge.predict_proba(X_teste)

	resultados = [resultados_bart , resultados_homer , resultados_lisa , resultados_maggie , resultados_marge]
	testes = [teste_bart , teste_homer , teste_lisa , teste_maggie , teste_marge]
	predicoes = combina_probabilidades(resultados)
	return predicoes	