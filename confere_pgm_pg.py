class ConferePGM:

    def carrega(self, path):
        _entrada = open(path, "rt")
        dados = _entrada.read().splitlines()
        return dados
        _entrada.close()

    def comparaLista(self, lista1, lista2):
        for dado in lista2:
            if dado[26:36] in lista1:
                print(dado)

def main():

    confere = ConferePGM()
    lista_pagos = confere.carrega("pagosPGM_distribuidorMai2018.txt")
    lista_problema = confere.carrega("07.txt")
    confere.comparaLista(lista_pagos, lista_problema)

if __name__ == "__main__":
    main()