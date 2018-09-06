class AjustaEdital:

    def carrega(self, path):
        entrada = open(path, "rt")
        dados = entrada.read().splitlines()
        entrada.close()
        return dados

    def separaNomeDoc(self, lista):
        doc = []
        self.nova_lista = []
        for dado in lista:
            if "CPF  " in dado or "CNPJ " in dado or "DOC.DEVEDOR" in dado:
                doc.append(dado[45:68])
                self.nova_lista.append(dado[0:44])
            elif len(doc) > 0:
                for documento in doc:
                    self.nova_lista.append(documento)
                doc.clear()
            else:
                self.nova_lista.append(dado)

    def grava(self, path):
        saida = open(path, "w")
        for dado in self.nova_lista:
            saida.write(dado + "\n")
        saida.close()

def main():

    prog = AjustaEdital()
    lista = prog.carrega("arquivos/Relatorio_Edital_Jornal_16_07_2018 (4).txt")
    prog.separaNomeDoc(lista)
    prog.grava("arquivos/Relatorio_Edital_Jornal_16_07_2018 (4)n.txt")

if __name__ == "__main__":
    main()