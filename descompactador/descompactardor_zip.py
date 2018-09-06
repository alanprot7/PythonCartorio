# coding: utf-8
import os
import zipfile
import sys

def main():

    arquivo = ""

    for dado in os.listdir():
        if "zip" in dado:
            arquivo = dado

    if not os.path.exists(arquivo):
        print("Arquivo {} não existe". format(arquivo))
        sys.exit(-1)
    else:
        zfile = zipfile.ZipFile(arquivo)
        zfile.extractall()
        zfile.close()
        os.system("del *.zip")


if __name__ == "__main__":
    main()