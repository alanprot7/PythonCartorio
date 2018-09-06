class EliminaRepetido:

    def carregaArquivo(self, caminho):
        _arquivo = open(caminho, "rt")
        dados = _arquivo.read().splitlines()
        _arquivo.close()
        return dados

    def listaUnicos(self, dados):
        dados_unicos = []

        for dado in dados:
            if dado not in dados_unicos:
                dados_unicos.append(dado)
                print(dado)

def main():

    unicos = EliminaRepetido()
    dados = unicos.carregaArquivo("arquivos/nova_lista.txt")
    unicos.listaUnicos(dados)

if __name__ == "__main__":
    main()