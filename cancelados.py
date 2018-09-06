class Cancelados:

    def carrega(self, path):
        entrada = open(path, "rt")
        dados = entrada.read().splitlines()
        entrada.close()
        return dados

    def tria(self, lista, palavra):
        for index, dado in enumerate(lista):
            if dado[11:12] == "." or dado[10:11] == ".":
                if palavra not in lista[index + 1]:
                    print(dado)
                    print(lista[index + 1])

def main():

    prog = Cancelados()
    lista = prog.carrega("arquivos/cancelados.txt")
    prog.tria(lista, "PROCURADORIA")

if __name__ == "__main__":
    main()