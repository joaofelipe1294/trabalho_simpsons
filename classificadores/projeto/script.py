import numpy as np
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

X = []
y = []
arquivo = open('caracteristicas.txt' , 'r')
for linha in arquivo:
	values_str = linha.split(',')
	contador = 0
	lista = []
	while contador < len(values_str):
		lista.append(values_str[contador])
		lista_float = []
		float_cont = 0

		while float_cont < len(lista) - 1:
			float_val = float(lista[float_cont])
			lista_float.append(float_val)
			float_cont += 1
		contador += 1
	X.append(lista_float)
	label = int(linha[len(linha) - 2])
	y.append(label)
X_scaled = preprocessing.normalize(X, norm='l2')
pca = PCA()
pca.fit(X_scaled)
#print(pca.explained_variance_ratio_) 
#print(X[0])

X_test_bart = [[0.2222222222135314950719476,0.0123456790099652734260527,0.0054869677900844437620775,0.0002194786945866612196034,-0.0000002408544962240974355,-0.0000243865216183765845634,-0.0000000000003426748561917,4.400440,0.000000,0.001549,0.000000,0.000000,0.000000,0.000000,0.000000]]
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_scaled, y)
print(neigh.predict(X_test_bart))
#print(neigh.predict_proba(X_test_bart))