class AdalbertoEndereco:

    def carrega(self, path):
        entrada = open(path, 'rt')
        dados = entrada.read().splitlines()
        entrada.close()
        return dados

    def geraEtiquetaMotivo(path, motivo, lista):
        lista_etiqueta = []
        for dado in lista:
            if len(dado) > 84:
                array_dado = dado.split(';')
                if motivo in dado:
                    texto = 'CARTORIO: {}        PROTOCOLO: {}     MOTIVO: {}\n{}'.format(array_dado[0], array_dado[1], array_dado[2], array_dado[5])
                    lista_etiqueta.append(texto)
        return lista_etiqueta

def main():

    app = AdalbertoEndereco()
    lista = app.carrega('C:/Users/AlanProt7/Documents/7º Oficio.csv')
    lista_mudou_se = app.geraEtiquetaMotivo('MUDOU-SE', lista)
    lista_endereco_incompleto = app.geraEtiquetaMotivo('ENDEREÇO INCOMPLETO', lista)

    '''for dado in lista_endereco_incompleto:
        print(dado)
        print('\n')'''

    for dado in lista_mudou_se:
        print(dado)
        print('\n')

if __name__ == '__main__':
    main()