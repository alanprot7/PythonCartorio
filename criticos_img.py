import os
import shutil

class ListaArqu:
    
    def listar(self, path):
        self._lista = []
        self.listarWalk(path)
        return self._lista
    
    def listarSub(self, path):
        for nome in os.listdir(path):
            arq = os.path.join(path, nome)
            if os.path.isfile(arq):
                self._lista.append(arq)
            else:
                self.listarSub(arq)

    def listarWalk(self, path):
        for caminho_diretorio, lista_diretorios, lista_arquivos in os.walk(path):
            for nome_arquivo in lista_arquivos:
                self._lista.append(os.path.join(caminho_diretorio, nome_arquivo))

def main():

    arq = ListaArqu()
    cont = 0
    path_pesquisa = "D:/BackupXP/Prot7/BxDoc/VEJA/P2P/SEGDOC/INTIMACOES_DIARIAS"
    path_lista = "F:/Projetos/XPROGs/CRITICOS/Files/Critico.txt"
    path_resultado = "P:/Imagem Críticos/"
    limpar(path_resultado)
    _pesquisa = open(path_lista)
    dados = _pesquisa.read().splitlines()
    dados_unicos = []
    print("iniciado leitura criticos")
    for dado in dados:
        if dado[:7] not in dados_unicos:
            dados_unicos.append(dado[:7])
    print("finalizado leitura criticos")
    print("iniciado listagem diretorios")

    '''opcao = 's' #input('Deseja atualizar a base?(s/n): ')

    if opcao == "s":
        listados = arq.listar(path_pesquisa)
        os.remove("criticos_img.ini")
        saida = open("criticos_img.ini", "w")
        for linha in listados:
            saida.write(linha + "\n")
        saida.close()
    else:
        entrada = open("criticos_img.ini", "rt")
        listados = entrada.read().splitlines()
        entrada.close()'''

    listados = arq.listar(path_pesquisa)

    print("listagem diretorios completo")
    for nome in listados:
        for dado in dados_unicos:
            if dado in nome:
                nome_arquivo = nome.split("\\")
                cont += 1
                print(cont, nome_arquivo[-1])
                shutil.copy2(nome, path_resultado + nome_arquivo[-2] + nome_arquivo[-1])
    _pesquisa.close()
    print("Total:", cont)
    os.system("pause")

def limpar(path):
    _lista = os.listdir(path)
    for nome in _lista:
        os.remove(os.path.join(path, nome))

if __name__ == "__main__":
    main()