class TestaSerasa:

    def carrega(self, path):
        _entrada = open(path, "rt")
        dados = _entrada.read().splitlines()
        _entrada.close()
        return dados

    def comparaDados(self, lista1, lista2):
        for dado in lista1:
            if dado not in lista2:
                print("Faltou protocolo:", dado)

    def lista(self, lista, tipo):
        lista_pesquisa = []
        for dado in lista:
            if dado[1:2] == tipo:
                lista_pesquisa.append(dado[450:457])
        return lista_pesquisa



def main():

    prog = TestaSerasa()

    P070706C = prog.carrega("arquivos/P070706C.txt")
    P070706pc = prog.carrega("arquivos/P070706pc.txt")
    P071004 = prog.carrega("arquivos/P071004.txt")
    P071104 = prog.carrega("arquivos/P071104.txt")
    P070706pach = prog.carrega("arquivos/P070706pach.txt")

    tipo = "C"

    prog.comparaDados(prog.lista(P070706pach, tipo), prog.lista(P071104, tipo))

if __name__ == "__main__":
    main()