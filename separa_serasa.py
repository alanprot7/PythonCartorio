from corrige_numero_linha import CorrigeNumeroLinha

class SeparaSerasa:

    def carrega(self, path):
        entrada = open(path, "rt")
        dados = entrada.read().splitlines()
        entrada.close()
        return dados

    def separa(self, lista, path):
        letras = ['a','b','c','d','e','f','g','h','i']
        letra = 0
        nova_lista = []
        header = lista[0]
        footer = lista[len(lista)-1]
        self.seq_ant = int(header[61:67])
        self.seq_novo = self.seq_ant
        lista.remove(header)
        lista.remove(footer)
        for dado in lista:
            nova_lista.append(dado)
            if len(nova_lista) == 950:
                self.gravar(path, nova_lista, header, footer, letras[letra])
                letra += 1
                nova_lista.clear()
        if len(nova_lista) > 0:
            self.gravar(path, nova_lista, header, footer, letras[letra])

    def gravar(self, path, lista, header, footer, letra):
        corrige = CorrigeNumeroLinha()
        self.seq_novo += 1
        header = header.replace("{:06d}".format(self.seq_ant), "{:06d}".format(self.seq_novo))
        novo_path = path[:-4] + letra + path[-4:]
        print(novo_path)
        saida = open(novo_path, "w")
        saida.write(header + "\n")
        for dado in lista:
            saida.write(dado + "\n")
        saida.write(footer)
        saida.close()
        corrige.carrega_arquivo(novo_path)
        corrige.grava_arquivo_novo(novo_path)

def main():

    prog = SeparaSerasa()
    path = "arquivos/P070307.txt"
    lista = prog.carrega(path)
    prog.separa(lista, path)

if __name__ == "__main__":
    main()
