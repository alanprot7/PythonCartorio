class NumeroRemessa:

    def __init__(self):
        self.remessa_menor = 999999
        self.remessa_maior = 0

    def verificaRemessa(self, dados):
        remessa = int(dados[0][61:67])
        if remessa < self.remessa_menor:
            self.remessa_menor = remessa
        if remessa > self.remessa_maior:
            self.remessa_maior = remessa

    def remessaMaior(self):
        return self.remessa_maior

    def remessaMenor(self):
        return self.remessa_menor