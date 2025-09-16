from automovel import Automovel


class AutomovelCarga(Automovel):
 
    def __init__(self):
        super().__init__()
        self.capacidade_carga = 0.0
        self.qtde_eixos = 0
 
    def ligar(self, qtde_eixos):
        self.qtde_eixos
        print("Caminhão ligando numero de eixos =" , self.qtde_eixos)
 
    def desligar(self):
        print("Caminhão desligando ....")