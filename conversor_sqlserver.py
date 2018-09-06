import os

class ConversorSqlServer:

    def carrega(self, path):
        entrada = open(path, 'rt')
        dados = entrada.read().splitlines()
        entrada.close()
        return dados

    def preparaInsert(self, lista, tabela):
        lista_insert = []
        tabela = tabela.replace('.txt','')
        for dado in lista:
            dado = dado.replace(' 00:00:00','')
            while True:
                if ',,' in dado:
                    dado = dado.replace(',,',',null,')
                else:
                    break
            if dado[-1:] == ',':
                dado = dado + 'null'
            dado = dado.replace('{',"'").replace('}',"'")
            dado = dado.replace('False', '0').replace('True','1')
            lista_insert.append('INSERT INTO {} VALUES({});'.format(tabela, dado))
        return lista_insert

    def gravaNovo(self, path, lista):
        saida = open(path, 'w')
        for dado in lista:
            saida.write(dado + '\n')
        saida.close()

def main():

    app = ConversorSqlServer()
    path = 'arquivos/bd'
    lista_diretorio = os.listdir(path)
    for nome in lista_diretorio:
        arquivo = app.carrega(os.path.join(path , nome))
        arquivo_novo = app.preparaInsert(arquivo, nome.lower())
        novo_caminho = os.path.join(path, nome.replace('.txt'.upper(),'(1).txt'.upper()))
        app.gravaNovo(novo_caminho, arquivo_novo)

if __name__ == '__main__':
    main()