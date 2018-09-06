class IntimacaoRemessa:


    def __init__(self, normal, correio):
        self._data_normal = normal
        self._data_correio = correio
        self._TAMANHO = 5

    def carregaArquivo(self, caminho):
        self._file = open(caminho, "rt")
        self._dados = self._file.read().splitlines()
        return self._dados
        self._file.close()

    def gravaArquivo(self, caminho, dados):
        self._out = open(caminho, "w")
        for dado in dados:
            if dado:
                self._out.write(dado + "\n")
        self._out.close()

    def juntaIntimacoes(self, atual, anterior ):
        self._data_n = self._data_normal + "100366000964401"
        self._data_c = self._data_correio + "100366000964401"
        for dado in anterior:
            if anterior:
                if self._data_n in dado or self._data_c in dado:
                    atual.append(dado)
        return atual


    def juntaRemessa(self, atual, anterior):
        self._data_n = self._data_normal.replace("/20","").replace("/","") + "00"
        self._data_c = self._data_correio.replace("/20","").replace("/","") + "00"
        self._atual_fim = atual[-1]
        atual.remove(self._atual_fim)
        for dado in anterior:
            if self._data_n in dado or self._data_c in dado:
                atual.append(dado)
        atual.append(self._atual_fim)
        atual = self.corrigeNumeracao(atual)
        return atual

    def juntaRemessaRejeitada(self, atual, anterior, lista):
        self._atual_fim = atual[-1]
        atual.remove(self._atual_fim)
        for dado in anterior:
            if dado[37:44] in lista:
                atual.append(dado.replace(dado[139:156], dado[139:154] + "16"))
        atual.append(self._atual_fim)
        atual = self.corrigeNumeracao(atual)
        return atual

    def corrigeNumeracao(self, dados):
        self._novo_dados = []
        for indice,dado in enumerate(dados):
            self._novo_dados.append(self.numeraLinha(dado, indice + 1))
        return self._novo_dados

    def numeraLinha(self, linha, numero):
        self._final = str(numero)
        while len(self._final) < self._TAMANHO:
            self._final = "0" + self._final
        return linha[:-5] + self._final

def main():

    intimacao = IntimacaoRemessa("13/08/2018","20/08/2018")
    anterior = intimacao.carregaArquivo("arquivos/CB030832.txt")
    atual = intimacao.carregaArquivo("arquivos/CB060832.txt")
    count = len(atual)
    lista = intimacao.carregaArquivo("arquivos/listaRejeitadosRemessaItau.txt")
    #resultado = intimacao.juntaIntimacoes(atual, anterior)
    resultado = intimacao.juntaRemessa(atual, anterior)
    #resultado = intimacao.juntaRemessaRejeitada(atual, anterior, lista)
    intimacao.gravaArquivo("arquivos/#RESULTADO.txt", resultado)
    print(len(resultado) - count)

if __name__ == "__main__":
    main()
