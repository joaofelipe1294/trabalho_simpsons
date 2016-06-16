def calcula_votos(votos):
	''' aplica a fusao de classificadores por meio de votos '''
	classes = []
	contador_votos = 0
	iteracoes_votos = len(votos[0])
	while contador_votos < iteracoes_votos:
		contador = 0
		iteracoes = len(votos)
		bart_votos = 0
		homer_votos = 0
		lisa_votos = 0
		maggie_votos = 0
		marge_votos = 0
		while contador < iteracoes:
			if votos[contador][contador_votos] == bart:
				bart_votos += 1

			elif votos[contador][contador_votos] == homer:
				homer_votos += 1

			elif votos[contador][contador_votos] == lisa:
				lisa_votos += 1

			elif votos[contador][contador_votos] == maggie:
				maggie_votos += 1

			elif votos[contador][contador_votos] == marge:
				marge_votos += 1			

			contador += 1


		if bart_votos > homer_votos and bart_votos > lisa_votos and bart_votos > maggie_votos and bart_votos > marge_votos:
			classes.append(bart)

		elif homer_votos > bart_votos and homer_votos > lisa_votos and homer_votos > maggie_votos and homer_votos > marge_votos:
			classes.append(homer)

		elif lisa_votos > bart_votos and lisa_votos > homer_votos and lisa_votos > maggie_votos and lisa_votos > marge_votos:
			classes.append(lisa)

		elif maggie_votos > bart_votos and maggie_votos > homer_votos and maggie_votos > lisa_votos and maggie_votos > marge_votos:
			classes.append(maggie)

		elif marge_votos > bart_votos and marge_votos > homer_votos and marge_votos > lisa_votos and marge_votos > lisa_votos:
			classes.append(marge)

		else:
			classes.append(marge)

		contador_votos += 1
	return classes



def soma(probabilidades):
	''' aplica fusao de classificadores por meio da soma '''
	classes = []
	contador_prob = 0
	iteracoes_prob = len(probabilidades[0])
	while contador_prob < iteracoes_prob:
		somas = [0 , 0 , 0 , 0, 0]
		contador_class = 0
		iteracoes_class = len(probabilidades)

		while contador_class < iteracoes_class:
			contador = 0
			iteracoes = len(probabilidades[0][0])
			while contador < iteracoes:
				somas[contador] += probabilidades[contador_class][contador_prob][contador]
				contador += 1
			contador_class += 1
			
		index_maior = 0
		maior = somas[0]
		contador = 0

		while contador < len(somas):
			if somas[contador] > maior:
				index_maior = contador
				maior = somas[contador]
			contador += 1
		classes.append(index_maior + 1)
		contador_prob += 1
	return classes













