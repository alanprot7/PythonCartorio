class Protocolo:

    def carrega(self, path):
        _entrada = open(path, "rt")
        dados = _entrada.read().splitlines()
        _entrada.close()
        return dados

    def exibeProtocolos(self, lista):
        for linha in lista:
            print(linha[316:323])

    def exibeSimples(self, lista):
        for dado in lista:
            print(dado[:7])

def main():

    prot = Protocolo()

    lista = prot.carrega("arquivos/edital.txt")

    #prot.exibeProtocolos(lista)
    prot.exibeSimples(lista)

if __name__ == "__main__":
    main()