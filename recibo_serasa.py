import os
from serasa_data import DiscriminaData
from serasa_num_remessa import NumeroRemessa

class ReciboSerasa:

    protestado_certidao = []
    protestado_auxiliar = 0
    cancelado_certidao = []
    cancelado_auxiliar = 0

    periodo = DiscriminaData()
    remessa = NumeroRemessa()

    def carrega_arquivo(self, caminho):
        self._file = open(caminho, "rt")
        self.data = self._file.read().split("\n")
        self._file.close()
        return self.data

    def lista_diretorio(self, diretorio):
        self.data_dir = os.listdir(diretorio)
        return self.data_dir

    def conta_certidoes(self, data):
        self.remessa.verificaRemessa(data)
        for self.dado in data:
            if self.dado:
                if "1CECEFLA" in self.dado:
                    self.data_ato = self.dado[477:485]
                    self.periodo.verifica_data(self.data_ato)
                    if self.data_ato not in self.cancelado_certidao:
                        self.cancelado_certidao.append(self.data_ato)
                    else:
                        self.cancelado_auxiliar += 1
                elif "1PICEFLA" in self.dado:
                    self.data_ato = self.dado[260:268]
                    self.periodo.verifica_data(self.data_ato)
                    if self.data_ato not in self.protestado_certidao:
                        self.protestado_certidao.append(self.data_ato)
                    else:
                        self.protestado_auxiliar += 1

    def printa_resultado(self):
        self.periodo.printa_periodos()
        print("Remessas:", self.remessa.remessaMenor(), "- a -", self.remessa.remessaMaior())
        print("Qtd Certidões Protesto:  %4d" % (len(self.protestado_certidao)))
        print("Qtd Auxiliar Protesto:   %4d" % (self.protestado_auxiliar))
        print("Qtd Certidões Cancelado: %4d" % (len(self.cancelado_certidao)))
        print("Qtd Auxiliar Cancelado:  %4d" % (self.cancelado_auxiliar))
                    
def main():

    recibo = ReciboSerasa()
    opcao = input("Calcular Serasa? (s/n): ")
    if opcao == "s":
        periodo = input("Digite o período (ex Jul2018): ")
        diretorio = "F:/Projetos/Serasa/2018/" + periodo
        print("Calculando Serasa...")
    else:
        print("Calculando Boa Vista...")
        diretorio = "F:/Projetos/Serasa/calculaBoaViasta"
    lista_arquivos = recibo.lista_diretorio(diretorio)

    for arquivo in lista_arquivos:
        data = recibo.carrega_arquivo(os.path.join(diretorio,arquivo))
        recibo.conta_certidoes(data)

    recibo.printa_resultado()
    os.system("pause")

if __name__ == "__main__":
    main()


