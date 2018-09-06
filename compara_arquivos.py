#coding: utf8

import os

class ComparaArquivos:

    def carregaArquivos(self, caminho):
        self._diretorio = os.listdir(caminho)
        self._dados = []
        for arq in self._diretorio:
            dado = open(caminho + arq, "rt")
            linhas = dado.read().splitlines()
            dado.close()
            self._dados.extend(linhas)
        return self._dados


    def preparaSerasa(self, dados):
        self._protocolo = []
        for linha in dados:
            self._protocolo.append(linha[450:457])
        return self._protocolo

    def preparaDist(self, dados):
        self._protocolo = []
        for linha in dados:
            self._protocolo.append(linha[447:457])
        return self._protocolo



    def comparaDados(self, dado1, dado2):
        for linha in dado1:
            if linha not in dado2:
                print(linha)

def main():

    compara = ComparaArquivos()
    dadoOk = compara.carregaArquivos("arquivos/distOk/")
    dadoErro = compara.carregaArquivos("arquivos/distErro/")
    dadoOk_prep = compara.preparaDist(dadoOk)
    dadoErro_prep = compara.preparaDist(dadoErro)

    compara.comparaDados(dadoErro_prep, dadoOk_prep)

    print(len(dadoErro) - len(dadoOk))

if __name__ == "__main__":
    main()