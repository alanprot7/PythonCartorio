class ChecaEdital(object):

	def carrega_arquivo(self, caminho):
		self._file = open(caminho, "rt")
		self.data = self._file.read().split("\n")
		self._file.close()
		return self.data

	def compara(self, arquivo1, arquivo2):
		self.igual = True

		for linha in arquivo1:
			if linha:
			    if linha not in arquivo2:
			        self.igual = False

		return self.igual

def main():

    checa = ChecaEdital()
    arquivo1 = checa.carrega_arquivo("arquivos/consultaEditalGermano280318.txt.txt")
    arquivo2 = checa.carrega_arquivo("arquivos/edital28032018.txt.txt")
   
    if checa.compara(arquivo1, arquivo2):
    	print("Arquivos iguais")
    else:
    	print("Arquivos diferentes")

if __name__ == "__main__":
	main()