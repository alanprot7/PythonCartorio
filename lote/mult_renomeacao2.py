import os

class MultRenomeacao:

    def carregaLista(self, caminho):
        self._arquivo = open(caminho, "rt")
        self._lista_nomes = self._arquivo.read().splitlines()
        self._arquivo.close()

    def listaArquivos(self, diretorio):
        self._caminho_diretorio = diretorio
        self._diretorio = os.listdir(self._caminho_diretorio)

    def renomeiaArquivos(self):
        self.verificaRepetido()
        for index, arquivo in enumerate(self._diretorio):
            origem = self._caminho_diretorio + arquivo
            destino = self._caminho_diretorio + self._lista_tratada[index]
            os.rename(origem, destino + ".tif")

    def totalResultado(self):
        print("Renomeados:" , len(self._diretorio))

    def verificaRepetido(self):
        cont = 1
        self._lista_tratada = []
        for nome in self._lista_nomes:
            if nome in self._lista_tratada:
                cont += 1
                self._lista_tratada.append(str(cont) + nome)
            else:
                self._lista_tratada.append(nome)

def main():


    renomeia = MultRenomeacao()
    renomeia.carregaLista("lista_nomes.txt")
    renomeia.listaArquivos("files/")
    renomeia.renomeiaArquivos()
    renomeia.totalResultado()
    os.system('pause')

if __name__ == "__main__":
    main()
