import os
from serasa_data import DiscriminaData
from serasa_num_remessa import NumeroRemessa

class ReciboSerasa:

    def __init__(self):
        self.protestado_certidao = []
        self.protestado_auxiliar = 0
        self.cancelado_certidao = []
        self.cancelado_auxiliar = 0
        self.mapa_aquivos_cancelados = {}
        self.mapa_aquivos_protestados = {}
        self.periodo = DiscriminaData()
        self.remessa = NumeroRemessa()

    def carrega_arquivo(self, caminho):
        _file = open(caminho, "rt")
        dados = []
        for data in _file:
            if len(data) > 0:
                dados.append(data + caminho)
        _file.close()
        return dados

    def lista_diretorio(self, diretorio):
        data_dir = os.listdir(diretorio)
        return data_dir

    def conta_certidoes(self, data):
        self.remessa.verificaRemessa(data)
        for dado in data:
            if dado:
                if "1CECEFLA" in dado:
                    data_ato = dado[477:485]
                    self.periodo.verifica_data(data_ato)
                    if data_ato not in self.cancelado_certidao:
                        self.cancelado_certidao.append(data_ato)
                    else:
                        self.cancelado_auxiliar += 1

                    chave_mapa = data_ato + dado[-18:-6].replace('\\','')
                    if chave_mapa not in self.mapa_aquivos_cancelados:
                        self.mapa_aquivos_cancelados[chave_mapa] = [data_ato,dado[-18:-6].replace('\\',''),dado[-4:],1]
                    else:
                        qtd = self.mapa_aquivos_cancelados[chave_mapa][3]
                        self.mapa_aquivos_cancelados[chave_mapa][3] = qtd + 1

                elif "1PICEFLA" in dado:
                    data_ato = dado[260:268]
                    self.periodo.verifica_data(data_ato)
                    if data_ato not in self.protestado_certidao:
                        self.protestado_certidao.append(data_ato)
                    else:
                        self.protestado_auxiliar += 1

                    chave_mapa = data_ato + dado[-18:-6].replace('\\','')
                    if chave_mapa not in self.mapa_aquivos_protestados:
                        self.mapa_aquivos_protestados[chave_mapa] = [data_ato, dado[-18:-6].replace('\\',''), dado[-4:], 1]
                    else:
                        qtd = self.mapa_aquivos_protestados[chave_mapa][3]
                        self.mapa_aquivos_protestados[chave_mapa][3] = qtd + 1

    def insereRemessa(self, dados):
        novo_dados = []
        for dado in dados:
            novo_dados.append(dado + dados[0][61:67])
        return novo_dados

    def printa_resultado(self):
        self.periodo.printa_periodos()
        print("Remessas:", self.remessa.remessaMenor(), "- a -", self.remessa.remessaMaior())
        print("Qtd Certidões Protesto:  {:4d}".format(len(self.protestado_certidao)))
        print("Qtd Auxiliar Protesto:   {:4d}".format(self.protestado_auxiliar))
        print("Qtd Certidões Cancelado: {:4d}".format(len(self.cancelado_certidao)))
        print("Qtd Auxiliar Cancelado:  {:4d}".format(self.cancelado_auxiliar))
                    
    def mostraMapa(self):
        cancelados = []
        protestados = []
        arquivos = []
        
        for key in self.mapa_aquivos_cancelados:
            cancelados.append(self.mapa_aquivos_cancelados[key])
        for key in self.mapa_aquivos_protestados:
            protestados.append(self.mapa_aquivos_protestados[key])

        cancelados.sort(key=self.getKey)
        for dado in cancelados:
            array = [dado[1], dado[2]]
            if array not in arquivos:
                arquivos.append(array)
        
        protestados.sort(key=self.getKey)
        for dado in protestados:
            array = [dado[1], dado[2]]
            if array not in arquivos:
                arquivos.append(array)

        gravar = []

        for nome in arquivos:
            gravar.append('Arquivo: ' + nome[0] + '  Remessa:  ' +  nome[1])
            for cancelado in cancelados:
                if cancelado[1] == nome[0]:
                    gravar.append('Data:  ' + cancelado[0] + '  Cancelados:  ' + str(cancelado[3]))
            for protestado in protestados:
                if protestado[1] == nome[0]:
                    gravar.append('Data:  ' +  protestado[0] +'  Protestados:  ' + str(protestado[3]))
            gravar.append('')

        self.grava(gravar)

    def getKey(self, item):
        return item[2]

    def grava(self, dados):
        saida = open('Relatorio.txt', 'w')
        for dado in dados:
            saida.write(dado + '\n')
        saida.close()

def main():

    app = ReciboSerasa()
    opcao = input("Calcular Serasa? (s/n): ")
    if opcao == "s":
        periodo = input("Digite o período (ex Jul2018): ")
        diretorio = "F:/Projetos/Serasa/2018/" + periodo
        print("Calculando Serasa...")
    else:
        print("Calculando Boa Vista...")
        diretorio = "F:/Projetos/Serasa/calculaBoaViasta"
    lista_arquivos = app.lista_diretorio(diretorio)

    for arquivo in lista_arquivos:
        data = app.carrega_arquivo(os.path.join(diretorio,arquivo))
        data = app.insereRemessa(data)
        app.conta_certidoes(data)

    app.printa_resultado()
    print('')
    app.mostraMapa()
    os.system("pause")

if __name__ == "__main__":
    main()