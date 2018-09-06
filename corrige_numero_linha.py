class CorrigeNumeroLinha(object):

    TAMANHO = 5

    def carrega_arquivo(self, caminho):
        self._file = open(caminho, "rt")
        self.data = self._file.read().split("\n")
        self._file.close()

    def numera_linha(self, linha, numero):
        self.final = str(numero)
        while len(self.final) < self.TAMANHO:
            self.final = "0" + self.final
        return linha + self.final

    def grava_arquivo_novo(self, caminho):
        self._saida = open(caminho, "w")
        for index,linha in enumerate(self.data):
            if linha:
                self.nova_linha = linha[:len(linha)-self.TAMANHO]
                self._saida.write(self.numera_linha(self.nova_linha,(index + 1)) + "\n")
        self._saida.close()

def main():

    numera = CorrigeNumeroLinha()

    numera.carrega_arquivo("C:/Users/AlanProt7/Documents/CB050432.txt")
    numera.grava_arquivo_novo("C:/Users/AlanProt7/Documents/CB050432(1).txt")

if __name__ == "__main__":
    main()