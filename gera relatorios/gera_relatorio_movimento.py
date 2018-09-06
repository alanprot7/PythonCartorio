import os
from gera_html import GeraHtml

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
                    "003020": 0,
                    "003021": 0,
                    "005023": 0,
                    "006012": 0,
                    "data": "" }
        data_inclusa = False

        for itens in self._lista_itens:
            for item in itens.getiterator():
                if item.tag == "codigo" and len(item.text) > 2:
                    if item.text in dic_lista:
                        dic_lista[item.text] += 1
                    else:
                        dic_lista[item.text] = 1
                if item.tag == "quantidadeExtra" and int(item.text) > 0:
                    dic_lista["adicionalPositiva"] += int(item.text)
                if not data_inclusa and item.tag == "data":
                    dic_lista[item.tag] = self.formataData(item.text)
                    data_inclusa = True

        return dic_lista

    def listaValores(self):
        dic_valores = {"001006": [0.00,0.00,0.00],
                    "003001":[0.00,0.00,0.00],
                    "003002": [0.00,0.00,0.00],
                    "003003": [0.00,0.00,0.00],
                    "003004": [0.00,0.00,0.00],
                    "003005": [0.00,0.00,0.00],
                    "003006": [0.00,0.00,0.00],
                    "003007": [0.00,0.00,0.00],
                    "003008": [0.00,0.00,0.00],
                    "003009": [0.00,0.00,0.00],
                    "003010": [0.00,0.00,0.00],
                    "003011": [0.00,0.00,0.00],
                    "003012": [0.00,0.00,0.00],
                    "003013": [0.00,0.00,0.00],
                    "003014": [0.00,0.00,0.00],
                    "003015": [0.00,0.00,0.00],
                    "003016": [0.00,0.00,0.00],
                    "003017": [0.00,0.00,0.00],
                    "003018": [0.00,0.00,0.00],
                    "003019": [0.00,0.00],
                    "003020": [0.00,0.00,0.00],
                    "003021": [0.00,0.00,0.00],
                    "005023": [0.00,0.00,0.00],
                    "006012": [0.00,0.00,0.00], }

        for itens in self._lista_itens:
            codigo_tabela = ""
            for item in itens.getiterator():
                if item.tag == "codigo" and len(item.text) > 2:
                    codigo_tabela = item.text
                if item.tag == "emolumento":
                    dic_valores[codigo_tabela][0] += float(item.text)
                if item.tag == "fermoju":
                    dic_valores[codigo_tabela][1] += float(item.text)
                if codigo_tabela != "003019" and item.tag == "ferc":
                    dic_valores[codigo_tabela][2] += float(item.text)

        return dic_valores

    def formataData(self, data):
        data = data.replace("-","/")
        return data[-2:] + data[4:8] + data[:4]

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
                listas_valores.append(leitor.listaValores())
        soma = 0

        for lista in listas_codigos:
            for key in lista.keys():
                if key not in dic_lista:
                    dic_lista[key] = lista[key]
                else:
                    if key != "data":
                        dic_lista[key] += lista[key]

        for lista in listas_valores:
            for key in lista.keys():
                if key not in dic_valores:
                    dic_valores[key] = lista[key]
                else:
                    dic_valores[key][0] += lista[key][0]
                    dic_valores[key][1] += lista[key][1]
                    if key != "003019":
                        dic_valores[key][2] += lista[key][2]

        for key in dic_lista.keys():
            if key != "adicionalPositiva" and key != "data":
                soma += dic_lista[key]

        

        relatorio = GeraHtml(dic_lista, dic_valores)
        relatorio.geraHtml()

        for arq in _arquivos:
            if ".xml" in arq:
                os.remove(arq)

        print("Relatório gerado com sucesso!")

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