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
        for index, arquivo in enumerate(self._diretorio):
            origem = self._caminho_diretorio + arquivo
            destino = self._caminho_diretorio + self._lista_nomes[index]
            os.rename(origem, destino + ".tif")

    def totalResultado(self):
        print("Renomeados:" , len(self._diretorio))

def main():


    renomeia = MultRenomeacao()
    renomeia.carregaLista("lista_nomes.txt")
    renomeia.listaArquivos("files/")
    renomeia.renomeiaArquivos()
    renomeia.totalResultado()
    os.system('pause')

if __name__ == "__main__":
    main()
