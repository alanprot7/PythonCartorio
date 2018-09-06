import os
from datetime import datetime

class Pesquisa:

    def __init__(self):
        self.now = datetime.now()
        self.titulos = []
    
    def carrega(self, path):
        entrada = open(path, "rt")
        dados = entrada.read().splitlines()
        entrada.close()
        return dados

    def listar(self, path):
        self._lista = []
        self.listarSub(path)
        return self._lista
    
    def listarSub(self, path):
        for nome in os.listdir(path):
            arq = os.path.join(path, nome)
            if os.path.isfile(arq):
                self._lista.append(arq)
            else:
                self.listarSub(arq)

    def busca(self, arquivo, cpnjs):
        for dado in arquivo:
            if dado[52:70] in cpnjs:
                data = dado[508:518].replace("/","")
                if len(data):
                    if self.comparaData(data):
                        print("Nome: " + dado[2:39] + " Limite: " + dado[508:518])
                        self.titulos.append("Nome: " + dado[2:70] + " Protocolo: " + dado[316:323] + " Limite: " + dado[508:518])

    def trata_data(self, data):
        self.data_int = int(data[-4:] + data[2:4] + data[:2])
        return self.data_int

    def comparaData(self, data):
        dia = "{:02}".format(self.now.day)
        mes = "{:02}".format(self.now.month)
        ano = "{}".format(self.now.year)
        if self.trata_data(data) >= self.trata_data(dia + mes + ano):
            return True
        else:
            return False

    def grava(self, path):
        saida = open(path, "w")
        for dado in self.titulos:
            saida.write(dado + "\n")
        saida.close()

        if len(self.titulos) == 0:
            print("Não foram encontrados títulos na Pesquisa\n")
            os.system("pause")
        else:
            os.system("pause")

def main():

    prog = Pesquisa()
    lista_arquivos = prog.listar("F:/Projetos/Notificacoes-STL/2018")
    cnpjs = prog.carrega("arquivos/CNPJsGildo.txt")
    for nome in lista_arquivos:
        if "BL07" in nome and "txt" in nome:
            arquivo = prog.carrega(nome)
            prog.busca(arquivo, cnpjs)
    prog.grava("resultadoGildo.txt")

if __name__ == "__main__":
    main()