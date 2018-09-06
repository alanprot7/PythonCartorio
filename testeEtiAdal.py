from tkinter import *

class EmiteEtiqu:

    def __init__(self, lista):
        self.lista = lista

    def msgShow(self, msg):
        janela = Tk()
        Label(janela, text = msg, font = ("Arial", 14)).pack()
        janela.mainloop( )

    def buscaProtocolo(self, protocolo):
        if protocolo not in self.lista:
            self.msgShow('Protocolo Não Encontrado: ' + protocolo)

def main():

    lista = ['1443865',
            '1443987',
            '1445666',
            '1446895',
            '1445658',
            '1304568']
            
    app = EmiteEtiqu(lista)

    print('Protocolos:')

    protocolo = input('')

    while protocolo != 'fim':
        app.buscaProtocolo(protocolo)
        protocolo = input('')

if __name__ == '__main__':
    main()