from PIL import Image
import os

class Rotacionar:

    def carrega(self, path):
        imagem = Image.open(path)
        return imagem

    def rotaciona(self, imagem, graus):
        imagem = imagem.rotate(graus)
        return imagem

    def gravaNova(self, imagem, path):
        imagem.save(path)

def main():

    app =  Rotacionar()
    list_arquivos = os.listdir()
    for nome_arquivo in list_arquivos:
        if 'ro_' not in nome_arquivo and '.tif' in nome_arquivo:
            imagem = app.carrega(nome_arquivo)
            imagem = app.rotaciona(imagem, 180)
            app.gravaNova(imagem, 'ro_' + nome_arquivo)
            os.remove(nome_arquivo)

if __name__ == '__main__':
    main()