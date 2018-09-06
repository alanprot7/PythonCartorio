import os
class ProtestoPGM:

    def carrega(self, path):
        entrada = open(path, "rt")
        dados = entrada.read().splitlines()
        entrada.close()
        return dados

    def busca(self, lista, palavra):
        for dado in lista:
            if palavra in dado:
                print(dado[:7])

def main():

    prog = ProtestoPGM()
    lista = prog.carrega("arquivos/protesto.txt")
    prog.busca(lista, "PROCURADORIA")
    os.system("pause")

if __name__ == "__main__":
    main()