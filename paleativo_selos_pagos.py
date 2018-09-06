class PaleativoPagos:

    def carrega(self, path):
        entrada = open(path, "rt")
        dados = entrada.read().splitlines()
        entrada.close()
        return dados

    def busca(self, lista_selos):
        for key in self.dicionario_pagos.keys():
            print(key)
            lista = []
            for protocolo in self.dicionario_pagos[key]:
                for dado in lista_selos:
                    if protocolo in dado:
                        prosicao = dado.index(protocolo)
                        lista.append(dado[prosicao:])
            lista.sort(key = self.getkey)
            for dado in lista:
                print(dado)

    def preparaListaPagos(self, lista):
        self.dicionario_pagos = {}
        for dado in lista:
            if "RELACAO DE TITULOS PAGOS E ENVIADOS AO APRESENTANTE:" in dado:
                apresentante = dado[53:]
                if apresentante not in self.dicionario_pagos:
                    self.dicionario_pagos[apresentante] = []
            if dado[:1] == "1":
                self.dicionario_pagos[apresentante].append(dado[:7])

    def getkey(self, item):
        return item[8:]

def main():

    prog = PaleativoPagos()
    lista_pagos = prog.carrega("arquivos/pagosApres.txt")
    lista_selos = prog.carrega("arquivos/selos.txt")
    prog.preparaListaPagos(lista_pagos)
    prog.busca(lista_selos)

if __name__ == "__main__":
    main()
