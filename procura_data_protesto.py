class ProcuraProtesto:

    def __init__(self):
        self.dados = []

    def carrega(self, path):
        entrada = open(path, "rt")
        dados = entrada.read().splitlines()
        for dado in dados:
            self.dados.append(dado)
        entrada.close()


    def buscaDataProtesto(self, data):
        for dado in self.dados:
            if data in dado:
                print(dado[450:457])

def main():

    prog = ProcuraProtesto()
    prog.carrega("arquivos/P072106.txt")
    prog.carrega("arquivos/P072206.txt")
    prog.carrega("arquivos/P072506.txt")
    prog.buscaDataProtesto("20062018")

if __name__ == "__main__":
    main()