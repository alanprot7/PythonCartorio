class PreparaArquivo(object):

	def carrega_e_prepara_arquivos(self, caminho1, caminho2):
		self._file1 = open(caminho1, "rt")
		self._file2 = open(caminho2, "rt")
		self.data1 = self._file1.read().split("\n")
		self.data2 = self._file2.read().split("\n")
		self._file1.close()
		self._file2.close()
		self._saida1 = open(caminho1+".txt", "w")
		self._saida2 = open(caminho2+".txt", "w")

		for linha in self.data1:
			if linha:
				self._saida1.write(linha[8:15]+"\n")
		self._saida1.close()

		for linha in self.data2:
			if linha:
				if linha[0:1] == "1":
				    self._saida2.write(linha[0:7]+"\n")
		self._saida2.close()

def main():
	
    prepara = PreparaArquivo()
    caminho1 = "arquivos/consultaEditalGermano280318.txt"
    caminho2 = "arquivos/edital28032018.txt"
    prepara.carrega_e_prepara_arquivos(caminho1, caminho2)

if __name__ == "__main__":
	main()
