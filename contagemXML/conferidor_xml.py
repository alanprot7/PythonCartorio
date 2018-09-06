import os

from xml.etree import ElementTree as et

class LeitorXml:

    def __init__(self):
        self._selo_certidao = []

    def acrescentaEstoqueSelo(self, selo_serie, serie_inicial, serie_final):
        serie_final += 1
        contador = serie_inicial
        for i in range(serie_inicial, serie_final):
            self._selo_certidao.append(selo_serie + str(i))

    def carregaArquivo(self, caminho):
        self._conteudo = et.parse(caminho)

    def defineItemProcura(self, item):
        self._lista_itens = self._conteudo.findall(item)

    def montaLista(self):
        dic_lista = {"adicionalPositiva": 0}
        dic_talao = []

        for itens in self._lista_itens:
            codigo = ""
            talao = ""
            data = ""
            for item in itens.getiterator():
                
                if item.tag == "talao":
                    talao = item.text
                if item.tag == "data":
                    data = item.text
                
                if item.tag == "codigo" and len(item.text) > 2:
                    codigo = item.text
                    if item.text in dic_lista:
                        dic_lista[item.text] += 1
                    else:
                        dic_lista[item.text] = 1
                
                if item.tag == "quantidadeExtra" and int(item.text) > 0:
                    dic_lista["adicionalPositiva"] += int(item.text)
                
                if codigo != "003009" and codigo != "003008" and codigo != "001006" and codigo != "003020":
                    if item.tag == "nrOrdemDistribuicaoTitulo" and not item.text:
                        if talao not in dic_talao:
                            dic_talao.append(talao)

                if codigo == "003009" or codigo == "003008" or codigo == "003020":
                    if item.tag == "serieInicial" and item.text not in self._selo_certidao:
                        print("Selo Inválido Certidao:", data, talao, item.text)



        for dado in dic_talao:
            print(dado, "Falta Protocolo do Distribuidor")

        return dic_lista

def main():

    
    leitor = LeitorXml()
    leitor.acrescentaEstoqueSelo("AJ", 704993, 705916 )
    leitor.acrescentaEstoqueSelo("AJ", 829817, 830614 )
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
        
#    for key in dic_lista.keys():
#        print(key, dic_lista[key])

    print("Total de Atos:", soma)
    os.system("pause")

if __name__ == "__main__":
    main()