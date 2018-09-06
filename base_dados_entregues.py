def trata(nome):
    return nome[3:]

def junta(nome, dados):
    return "{} {}".format(nome, dados)

def carrega_arquivo(caminho):
    _file = open(caminho, "rt")
    data = _file.read().split("\n")
    _file.close()
    return data

def main():

    for nome in carrega_arquivo("entregas20032018.txt"):
        if nome:
            imprimivel = junta(trata(nome),"20/03/2018 ENTREGUE")
            print(imprimivel)

if __name__ == "__main__":
    main()
