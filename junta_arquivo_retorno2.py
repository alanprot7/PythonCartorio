import os

class JuntaRetorno(object):
    
    def carrega_arquivo(self, caminho):
        self._file = open(caminho, "rt")
        self.data = self._file.read().split("\n")
        self._file.close()
        return self.data

    def mescla_movimento(self, arquivo1, arquivo2):
        self.data_arquivo = []
        for linha in arquivo1:
            if linha:
                self.data_arquivo.append(linha)
        self.data_arquivo.remove(arquivo1[-2])

        for linha in arquivo2:
            if linha:
                self.data_arquivo.append(linha)
        
        self.data_arquivo.remove(arquivo2[0])
        self.data_arquivo.remove(arquivo2[-2])

        self.data_arquivo.append(arquivo1[-2])
        return self.data_arquivo

    def numera_linha(self, linha, numero):
        return linha[:len(linha) - 4] + self.ajusta_numero(numero, 4)

    def soma_valores(self, arquivo):
        self.valor = 0
        for linha in arquivo:
            if linha:
                if linha[260:274].isnumeric():
                    self.valor += int(linha[260:274])
        return self.valor

    def ajusta_numero(self, numero, casas):
        self.numero_str = str(numero)
        while len(self.numero_str) < casas:
            self.numero_str = "0" + self.numero_str
        return self.numero_str


def main():

    junta = JuntaRetorno()

    mesclado = []
    arquivo1 = junta.carrega_arquivo("F:/Retornos/R0730204-23.181")
    arquivo2 = junta.carrega_arquivo("F:/Retornos/R0730204-27-28.181")
    #arquivo3 = junta.carrega_arquivo("F:/Retornos/R0012603.181")
    #arquivo4 = junta.carrega_arquivo("F:/Retornos/R0012703.181")


    mesclado = junta.mescla_movimento(arquivo1 , arquivo2)
    #mesclado.append("")
    #mesclado = junta.mescla_movimento(mesclado , arquivo3)
    #mesclado.append("")
    #mesclado = junta.mescla_movimento(mesclado , arquivo4)

    
    valor_somado = junta.soma_valores(mesclado)
    valor_str = junta.ajusta_numero(valor_somado , 18)
    mesclado[-1] = mesclado[-1].replace(mesclado[-1][57:75], valor_str)
    contagem = junta.ajusta_numero(len(mesclado) - 2 , 5)
    mesclado[-1] = mesclado[-1].replace(mesclado[-1][52:57], contagem)
    contagem_cabecalho = contagem[1:]
    mesclado[0] = mesclado[0].replace(mesclado[0][67:71], contagem_cabecalho)

    _saida = open("F:/Retornos/novo_retorno.txt", "w")

    for index,linha in enumerate(mesclado):
        _saida.write(junta.numera_linha(linha , index + 1)+"\n")

    _saida.close()

    #os.system("notepad.exe Retorno/teste.txt")

if __name__ == "__main__":
    main()