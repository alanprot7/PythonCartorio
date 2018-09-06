import os

from xml.etree import ElementTree as et

class LeitorXml:

    def carregaArquivo(self, caminho):
        self._conteudo = et.parse(caminho)

    def defineItemProcura(self, item):
        self._lista_itens = self._conteudo.findall(item)

    def montaLista(self):
        dic_lista = {"adicionalPositiva": 0,
                    "001006": 0,
                    "003001": 0,
                    "003002": 0,
                    "003003": 0,
                    "003004": 0,
                    "003005": 0,
                    "003006": 0,
                    "003007": 0,
                    "003008": 0,
                    "003009": 0,
                    "003010": 0,
                    "003011": 0,
                    "003012": 0,
                    "003013": 0,
                    "003014": 0,
                    "003015": 0,
                    "003016": 0,
                    "003017": 0,
                    "003018": 0,
                    "003019": 0,
                    "003021": 0,
                    "005023": 0,
                    "006012": 0,
                    "data": "" }


        for itens in self._lista_itens:
            for item in itens.getiterator():
                if item.tag == "codigo" and len(item.text) > 2:
                    if item.text in dic_lista:
                        dic_lista[item.text] += 1
                    else:
                        dic_lista[item.text] = 1
                if item.tag == "quantidadeExtra" and int(item.text) > 0:
                    dic_lista["adicionalPositiva"] += int(item.text)
 
        return dic_lista

def main():

    try:
        leitor = LeitorXml()
        _arquivos = os.listdir()
        listas_codigos = []
        listas_valores = []
        dic_lista = {}
        dic_valores = {}

        for arq in _arquivos:
            if ".xml" in arq:
                leitor.carregaArquivo(arq)
                leitor.defineItemProcura("item")
                listas_codigos.append(leitor.montaLista())
        soma = 0

        for lista in listas_codigos:
            for key in lista.keys():
                if key not in dic_lista:
                    dic_lista[key] = lista[key]
                else:
                    if key != "data":
                        dic_lista[key] += lista[key]

        for key in dic_lista.keys():
            if key != "adicionalPositiva" and key != "data":
                soma += dic_lista[key]
        
        for key in dic_lista.keys():
            print(key, dic_lista[key])


        print("Total de Atos:", soma)

        os.system("pause")


    except Exception:
        print("Ops!! Aconteceu um ERRO, talvez o arquivo esteja corrompido ou não existe.")
        print()
        print("Verifique se a pasta tem arquivos xml depois tente novamente.")
        print()

        os.system("pause")


if __name__ == "__main__":
    main()