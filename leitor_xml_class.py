from xml.etree import ElementTree as et

class LeitorXml:

    def carregaArquivo(self, caminho):
        self._conteudo = et.parse(caminho)

    def defineItemProcura(self, item):
        self._lista_itens = self._conteudo.findall(item)

    def montaLista(self):
        for itens in self._lista_itens:
            for item in itens.getiterator():
                if item.tag == "codigo" and len(item.text) > 2:
                	print(item.tag, item.text)
                if item.tag == "talao":
                	print(item.text)
                if item.tag == "fermoju":
                	print(item.text)
                if item.tag == "cpfCnpj":
                	print(item.text)
def main():

    leitor = LeitorXml()
    leitor.carregaArquivo("arquivos/SAIDA-PR-16042018-000307.xml")
    leitor.defineItemProcura("item")
    leitor.montaLista()


if __name__ == "__main__":
    main()