from Automovel import Automovel
from AutomovelCarga import AutomovelCarga


c = AutomovelCarga()
c.marca =  input('Informe a Marca do veiculo:')
c.modelo =  input('Informe o Modelo do veiculo:')
c.ano =  input('Informe o ano do veiculo:')
c.chassi =  input('Informe a Chassi do veiculo:')
c.cor =  input('Informe a Cor do veiculo:')
c.placa =  input('Informe a Placa do veiculo:')
c.qtde_eixos = input('Informe a Qtde de Eixos do Veiculo:')
c.capacidade_carga = input('Informe a capacidade de carga do Veiculo:')
c.ligar(c.qtde_eixos)
c.desligar()