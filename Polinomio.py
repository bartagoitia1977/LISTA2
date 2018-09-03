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
# Descricao:  Classe Polinomio questão 1 LISTA2
#
# Licenca: Copyright(c) 2018 Bruno Artagoitia Vicente do Nascimento
#
###############################################################################

import numpy as np

class Polinomio:
	def __init__ (self, A, B = None, C = None, D = None):
		self.__A = A
		self.__B = B
		self.__C = C
		self.__D = D
		self.__vect3 = np.array([self.__A,self.__B,self.__C,self.__D])
		self.__vect2 = np.array([self.__A,self.__B,self.__C])
		self.__vect1 = np.array([self.__A,self.__B])
		self.__vect0 = np.array([self.__A])
		self.__grau = -1
		self.__polistring = "f(x) = "
		self.__reprstring = "Polinomio("
		self.__cheese = 1
		self.__resultado = 0
		self.__apontador = 0
		self.__item = None
		for self.__x in self.__vect3:
			if (self.__x != None):
				self.__grau += 1
		if (self.__grau == 0):
			self.__poli = self.__vect0
		if (self.__grau == 1):
			self.__poli = self.__vect1
		if (self.__grau == 2):
			self.__poli = self.__vect2
		if (self.__grau == 3):
			self.__poli = self.__vect3
		self.__deri0 = None
		self.__deri1 = None
		self.__deri2 = None
				
	def __str__ (self):
		self.__polistring = "f(x) = "
		self.__count = 0
		if (self.__grau == 3):
			self.__exp = self.__grau
			while (self.__count < 3):
				self.__monomio = self.__poli[self.__count]
				if (self.__monomio > 0):
					if (self.__monomio != 1):
						if (self.__exp > 1):
							self.__polistring += "+"+str(self.__monomio)+"x^"+str(self.__exp)
						else:
							self.__polistring += "+"+str(self.__monomio)+"x"
					if (self.__monomio == 1):
						if (self.__exp > 1):
							self.__polistring += "+x^"+str(self.__exp)
						else:
							self.__polistring += "+x"

				if (self.__monomio < 0):
					if (self.__monomio != -1):
						if (self.__exp > 1):
							self.__polistring += str(self.__monomio)+"x^"+str(self.__exp)
						else:
							self.__polistring += str(self.__monomio)+"x"
					if (self.__monomio == -1):
						if (self.__exp > 1):
							self.__polistring += "-x^"+str(self.__exp)
						else:
							self.__polistring += "-x"

				self.__count += 1
				self.__exp -= 1
			self.__monomio = self.__poli[3]
			if (self.__monomio < 0):
				self.__polistring += str(self.__monomio)
			if (self.__monomio > 0):
				self.__polistring += "+"+str(self.__monomio)
			if (self.__monomio == 0):
				pass

		if (self.__grau == 2):
			self.__exp = self.__grau
			while (self.__count < 2):
				self.__monomio = self.__poli[self.__count]
				if (self.__monomio > 0):
					if (self.__monomio != 1):
						if (self.__exp > 1):
							self.__polistring += "+"+str(self.__monomio)+"x^"+str(self.__exp)
						else:
							self.__polistring += "+"+str(self.__monomio)+"x"
					if (self.__monomio == 1):
						if (self.__exp > 1):
							self.__polistring += "+x^"+str(self.__exp)
						else:
							self.__polistring += "+x"

				if (self.__monomio < 0):
					if (self.__monomio != -1):
						if (self.__exp > 1):
							self.__polistring += str(self.__monomio)+"x^"+str(self.__exp)
						else:
							self.__polistring += str(self.__monomio)+"x"
					if (self.__monomio == -1):
						if (self.__exp > 1):
							self.__polistring += "-x^"+str(self.__exp)
						else:
							self.__polistring += "-x"

				self.__count += 1
				self.__exp -= 1
			self.__monomio = self.__poli[2]
			if (self.__monomio < 0):
				self.__polistring += str(self.__monomio)
			if (self.__monomio > 0):
				self.__polistring += "+"+str(self.__monomio)
			if (self.__monomio == 0):
				pass
				
		if (self.__grau == 1):
			self.__monomio = self.__poli[0]
			if (self.__monomio > 0):
				if (self.__monomio != 1):
					self.__polistring += "+"+str(self.__monomio)+"x"
				if (self.__monomio == 1):
					self.__polistring += "+x"
			if (self.__monomio < 0):
				if (self.__monomio != -1):
					self.__polistring += str(self.__monomio)+"x"
				if (self.__monomio == -1):
					self.__polistring += "-x"
			self.__monomio = self.__poli[1]
			if (self.__monomio < 0):
				self.__polistring += str(self.__monomio)
			if (self.__monomio > 0):
				self.__polistring += "+"+str(self.__monomio)
			if (self.__monomio == 0):
				pass

		if (self.__grau == 0):
			self.__monomio = self.__poli[0]
			self.__polistring = str(self.__monomio)

		return self.__polistring

	def __call__(self,cheese):
		self.__resultado = 0
		self.__cheese = cheese
		self.__count = 0
		if (self.__grau == 3):
			self.__exp = self.__grau
			while (self.__count <= 3):
				self.__monomio = self.__poli[self.__count]
				self.__resultado += (self.__monomio * (self.__cheese ** self.__exp))
				self.__count += 1
				self.__exp -= 1

		if (self.__grau == 2):
			self.__exp = self.__grau
			while (self.__count <= 2):
				self.__monomio = self.__poli[self.__count]
				self.__resultado += (self.__monomio * (self.__cheese ** self.__exp))
				self.__count += 1
				self.__exp -= 1

		if (self.__grau == 1):
			self.__exp = self.__grau
			while (self.__count <= 1):
				self.__monomio = self.__poli[self.__count]
				self.__resultado += (self.__monomio * (self.__cheese ** self.__exp))
				self.__count += 1
				self.__exp -= 1

		if (self.__grau == 0):
			self.__resultado = self.__poli[0]

		return self.__resultado

	def __getitem__(self,indice):
		self.__indice = indice
		if (self.__grau == 3):
			if (self.__indice == 0):
				return self.__poli[3]
			if (self.__indice == 1):
				return self.__poli[2]
			if (self.__indice == 2):
				return self.__poli[1]
			if (self.__indice == 3):
				return self.__poli[0]
			if (self.__indice > 3) or (self.__indice < 0):
				raise ArithmeticError
		if (self.__grau == 2):
			if (self.__indice == 0):
				return self.__poli[2]
			if (self.__indice == 1):
				return self.__poli[1]
			if (self.__indice == 2):
				return self.__poli[0]
			if (self.__indice > 2) or (self.__indice < 0):
				raise ArithmeticError
		if (self.__grau == 1):
			if (self.__indice == 0):
				return self.__poli[1]
			if (self.__indice == 1):
				return self.__poli[0]
			if (self.__indice > 1) or (self.__indice < 0):
				raise ArithmeticError
		if (self.__grau == 0):
			if (self.__indice == 0):
				return self.__poli[0]
			if (self.__indice != 0):
				raise ArithmeticError

	def __repr__(self):
		self.__reprstring = "Polinomio("
		for self.__char in self.__poli:
			self.__reprstring += str(self.__char) + ","
		self.__reprstring = self.__reprstring[:-1] + ")"
		return self.__reprstring

	def derivada(self):

		if (self.__grau == 3):
			self.__deri0 = (self.__poli[0]*3)
			self.__deri1 = (self.__poli[1]*2)
			self.__deri2 = self.__poli[2]
			return Polinomio(self.__deri0,self.__deri1,self.__deri2)

		if (self.__grau == 2):
			self.__deri0 = (self.__poli[0]*2)
			self.__deri1 = self.__poli[1]
			return Polinomio(self.__deri0,self.__deri1)

		if (self.__grau == 1):
			self.__deri0 = self.__poli[0]
			return Polinomio(self.__deri0)

		if (self.__grau == 0):
			return Polinomio(0)

	def __iter__(self):
		self.__apontador = 0
		return self
		
	def __next__(self):
		self.__item = None
		if (self.__grau == 3):
			if (self.__apontador <= 3):
				self.__item = self.__poli[self.__apontador]
				self.__apontador += 1
				return self.__item
			else:
				raise StopIteration

		if (self.__grau == 2):
			if (self.__apontador <= 2):
				self.__item = self.__poli[self.__apontador]
				self.__apontador += 1
				return self.__item
			else:
				raise StopIteration

		if (self.__grau == 1):
			if (self.__apontador <= 1):
				self.__item = self.__poli[self.__apontador]
				self.__apontador += 1
				return self.__item
			else:
				raise StopIteration

		if (self.__grau == 0):
			if (self.__apontador <= 0):
				self.__item = self.__poli[self.__apontador]
				self.__apontador += 1
				return self.__item
			else:
				raise StopIteration