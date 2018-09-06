def trata(nome):
    return nome[6:]

def junta(nome, dados):
    return "{} {}".format(nome, dados)

def carrega_arquivo(caminho):
    _file = open(caminho, "rt")
    data = _file.read().split("\n")
    _file.close()
    return data

def main():

    for index,nome in enumerate(carrega_arquivo("intimacoesOutrosCartorios.txt")):
        if nome:
            indice = " {:2} -".format(index+1)
            imprimivel = junta(indice,trata(nome))
            print(imprimivel.replace("*",""))

if __name__ == "__main__":
    main()
