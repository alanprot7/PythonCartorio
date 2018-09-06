import os
from datetime import datetime

class Pesquisa:

    def __init__(self, data):
        self.now = datetime.now()
        self.titulos = []
        self.data_usuario = data
    
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
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                self._lista.append(os.path.join(root, name))

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
        if self.data_usuario:
            dia_usu = self.data_usuario[:2]
            mes_usu = self.data_usuario[2:4]
            ano_usu = self.data_usuario[-4:]
        else:
            dia_usu = dia
            mes_usu = mes
            ano_usu = ano
        if self.trata_data(data) >= self.trata_data(dia + mes + ano) or self.trata_data(data) >= self.trata_data(dia_usu + mes_usu + ano_usu):
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

    data_usuario = input('Informe data (ex: 23082018): ')
    prog = Pesquisa(data_usuario)
    lista_arquivos = prog.listar("F:/Projetos/Notificacoes-STL/2018")
    cnpjs = prog.carrega("arquivos/CNPJsGildo.txt")
    for nome in lista_arquivos:
        if "BL07" in nome and "txt" in nome:
            arquivo = prog.carrega(nome)
            prog.busca(arquivo, cnpjs)
    prog.grava("resultadoGildo.txt")

if __name__ == "__main__":
    main()