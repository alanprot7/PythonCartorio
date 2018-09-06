class BuscaDataMaior:

    def carrega(self, path):
        _entrada = open(path, "rt")
        dados = _entrada.read().splitlines()
        _entrada.close()
        return dados

    def preparaListaPesquisa(self, lista_edital):
        lista = []
        for protocolo in lista_edital:
            lista.append(protocolo[-7:])
        return lista

    def comparaListas(self, lista_pesquisa, lista_sinc):
        cont = 0
        for protocolo in lista_sinc:
            if protocolo[506:513] in lista_pesquisa:
                data = protocolo[536:544]
                if data == "01062018":
                    cont += 1
                    print (protocolo[506:513], data)
        print("Total:", cont)

def main():

    program = BuscaDataMaior()

    lista_edital = program.carrega("edital30052018.txt")
    lista_sinc = program.carrega("SINC3005.TXT")
    lista_pesquisa = program.preparaListaPesquisa(lista_edital)
    program.comparaListas(lista_pesquisa, lista_sinc)

if __name__ == "__main__":
    main()