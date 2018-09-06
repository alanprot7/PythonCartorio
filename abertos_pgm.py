class AbertoPGM:

    def carrega(self, path):
        entrada = open(path, "rt")
        dados = entrada.read().splitlines()
        entrada.close()
        return dados

    def comparar(self, abertos, retorno):
        protocolos = []
        for dado in retorno:
            if dado[447:448] == "7":
                protocolos.append(dado[447:457])

        for dado in abertos:
            if dado[3:13] not in protocolos:
                print(dado[3:13])

def main():

    app = AbertoPGM()
    abertosPGM = app.carrega("arquivos/abertosPGM.txt")
    retornoPGM = app.carrega("arquivos/R0730309.181")
    app.comparar(abertosPGM, retornoPGM)

    #abertosPGFN = app.carrega("arquivos/abertoPGFN.txt")
    #retornoPGFN = app.carrega("arquivos/R0673107.181") 
    #app.comparar(abertosPGFN, retornoPGFN)

if __name__ == "__main__":
    main()
