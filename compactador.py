import zipfile
import os
class Compactador:

    def compactar(self, path):
        zip_path = path[:-4] + '.zip'
        zfile = zipfile.ZipFile(zip_path, 'w')
        zfile.write(path, os.path.basename(path),compress_type = zipfile.ZIP_DEFLATED)
        zfile.close()

def main():

    app = Compactador()
    app.compactar('F:/Projetos/Retorno Dist/BA310818.007')

if __name__ == '__main__':
    main()
