import os
from datetime import datetime

class CanceladosSemCusta:

    def __init__(self):
        self.now = datetime.now()

    def carrega(self, path):
        entrada = open(path, "rt")
        dados = entrada.read().splitlines()
        entrada.close()
        return dados

    def listaDiretorio(self, path):
        lista = os.listdir(path)
        lista_com_caminho = []
        
        for nome in lista:
            if "18.007" in nome:
                lista_com_caminho.append(os.path.join(path,nome))

        return lista_com_caminho

    def preparaListaCra(self, lista):
        lista_protocolos = []
        for dado in lista:
            lista_protocolos.append(dado[0:10])
        return lista_protocolos

    def comparaListas(self, lista_protocolos, listaDiretorio, lista_cra):
        lista_escrita = []
        for nome_arquivo in listaDiretorio:
            arquivo = self.carrega(nome_arquivo)
            for dado in arquivo:
                if len(dado) > 457 and dado[447:448] == "7":
                    if dado[447:457] in lista_protocolos:
                        lista_protocolos.remove(dado[447:457])

        if len(lista_cra) > 0:
            dia = "{:02}".format(self.now.day)
            mes = "{:02}".format(self.now.month)
            ano = "{}".format(self.now.year)
            lista_escrita.append('---------------------------------------------------------------------------------')
            lista_escrita.append('Lista de Títulos Cancelados Sem custa em {}/{}/{}'.format(dia, mes, ano))
            lista_escrita.append('---------------------------------------------------------------------------------\n')
            for dado in lista_cra:
                if dado[0:10] in lista_protocolos:
                    lista_escrita.append(dado)
            lista_escrita.append('---------------------------------------------------------------------------------')

        self.grava(lista_escrita)

    def grava(self, lista):
        saida = open('SemOnus.txt', 'w')
        for dado in lista:
            saida.write(dado + '\n')
        saida.close()


def main():

    app = CanceladosSemCusta()
    lista_diretorio = app.listaDiretorio("F:/Projetos/Retorno Dist")
    lista_cra = app.carrega("arquivos/listaCRA.txt")
    lista_protocolos = app.preparaListaCra(lista_cra)
    app.comparaListas(lista_protocolos, lista_diretorio, lista_cra)


if __name__ == "__main__":
    main()