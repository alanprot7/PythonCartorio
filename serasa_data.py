

class DiscriminaData:
    
    data_maior = "0"
    data_menor = "99999999"

    def verifica_data(self, data):
        if(self.trata_data(data) < self.trata_data(self.data_menor)):
        	self.data_menor = data
        if(self.trata_data(data) > self.trata_data(self.data_maior)):
        	self.data_maior = data

    def trata_data(self, data):
        data_int = int(data[-4:] + data[2:4] + data[:2])
        return data_int


    def printa_periodos(self):
        print("Período %s - a - %s" % (self.data_menor, self.data_maior))
