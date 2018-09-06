class DevolvidasAvulsas(object):

    def carrega_arquivo(self, caminho):
        self._file = open(caminho, "rt")
        self.data = self._file.read().split("\n")
        self._file.close()
        return self.data

    def formata_nome(serf, nome):
        return nome[7:14]

def main():

    devolvidos = DevolvidasAvulsas()

    lista = devolvidos.carrega_arquivo("devolvidas_avulsas.txt")
    for linha in lista:
        if linha:
            print("%s 26/03/2018 DEVOLVIDA" % (devolvidos.formata_nome(linha)))

if __name__ == "__main__":
    main()
