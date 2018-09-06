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

    for nome in carrega_arquivo("erroEdital.txt"):
        if nome:
            imprimivel = nome[0:7]
            print(imprimivel)

if __name__ == "__main__":
    main()
