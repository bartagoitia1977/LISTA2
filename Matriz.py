###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF969 -- Algoritmos e Estruturas de Dados
#
# Autor:    Bruno Artagoitia Vicente do Nascimento
# Email:    bavn@cin.ufpe.br
# Data:        2018-09-05
#
# Descricao:  Classe Matriz questão 2 LISTA2
#
# Licenca: Copyright(c) 2018 Bruno Artagoitia Vicente do Nascimento
#
###############################################################################

import numpy as np

class Matriz:

	def __init__(self,linhas,colunas):
		self.__linhas = linhas
		self.__colunas = colunas
		self.__vetlinha = np.zeros(self.__colunas,int)
		self.__vetor = np.zeros((self.__linhas,self.__colunas),int)
		self.__matstring = "["
		self.__matstring_linha = "["
		self.__tam = 0
		for self.__strc in self.__vetlinha:
			self.__matstring_linha += str(self.__strc) + ","
		self.__matstring_linha = self.__matstring_linha[:-1] + "]"
		for self.__strl in range(self.__linhas):
			self.__matstring += self.__matstring_linha + ","
		self.__matstring = self.__matstring[:-1] + "]"

	def __getitem__(self,indice0,indice1 = None):
		self.__indice0 = indice0
		self.__indice1 = indice1
		if (self.__indice1 == None):
			return self.__vetor[self.__indice0]
		else:
			return self.__vetor[self.__indice0][self.__indice1]
		
	def __str__(self):
		return self.__matstring

	def __repr__(self):
		return "Matriz("+str(self.__linhas)+","+str(self.__colunas)+")"

