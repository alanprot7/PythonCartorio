class DigilocCEP:
    
    def carregaArquivo(self, caminho):
        self._file = open(caminho, "rt")
        self.dados = self._file.read().split("\n")
        self._file.close()
        return self.dados

    def gravaArquivo(self, caminho):
        self._out = open(caminho, "w")
        for dado in self.dados_ordenados:
            if dado:
                self._out.write(dado + "\n")
        self._out.close()

    def getKey(self, item):
        return item[424:433]

    def ordenaDados(self, dados):
        self.dados_ordenados = dados
        self.dados_ordenados.sort(key = self.getKey)
        return self.dados_ordenados

def main():

    digiloc = DigilocCEP()

    dados = digiloc.carregaArquivo("D:/Google Drive/Python/Cartorio/arquivos/BL072003.txt")
    digiloc.ordenaDados(dados)
    digiloc.gravaArquivo("D:/Google Drive/Python/Cartorio/arquivos/BL072003(1).txt")

if __name__ == "__main__":
    main()