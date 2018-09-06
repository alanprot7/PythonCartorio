class ComparaDiferenca:

    def carrega(self, path):
        entrada = open(path, "rt")
        dados = entrada.read().splitlines()
        entrada.close()
        return dados

    def compara(self, lista_maior, lista_menor):
        separador = []
        for dado in lista_menor:
            protocolo = dado[188:198]
            if protocolo not in separador:
                separador.append(protocolo)

        for dado in lista_maior:
            protocolo = dado[188:198]
            if protocolo not in separador:
                print(dado)

def main():

    prog = ComparaDiferenca()
    lista_maior = prog.carrega("arquivos/BL072506maior.txt")
    lista_menor = prog.carrega("arquivos/BL072506.txt")
    prog.compara(lista_maior, lista_menor)

if __name__ == "__main__":
    main()