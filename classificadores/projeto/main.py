from sys import argv
from functions import *
from funcoes_de_classificacao import *
from lda_funcoes import *
from svm_funcoes import *
from knn_funcoes import *
from tree_funcoes import *

""" CONSTANTES """
bart = 1
homer = 2
lisa = 3
maggie = 4
marge = 5   



""" prepara dados """
dir_treino = argv[1]
dir_validacao = argv[2]
X_treino , y_treino = prepara_dados('treino.txt')
X_teste , y_teste = prepara_dados('validacao.txt')



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


'''
""" MLP """
print("========== MLP ==========")
mlp_predicoes = MLP_resultados(X_treino , y_treino , X_teste , y_teste)
exibe_resultados(mlp_predicoes , y_teste)
'''