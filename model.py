import requests
import pandas as pd

class ViaCEP:
    def __init__(self):
        self.url = "https://viacep.com.br/ws"

    def chamar_cep(self, cep_consulta):
        return requests.get(f"{self.url}/{cep_consulta}/json")

    def chamar_enderenco(self, estado, cidade, rua):
        return requests.get(f"{self.url}/{estado}/{cidade}/{rua}/json")

    def retorna_json(self,resposta):
        return resposta.json()

    def retorna_csv(self,json):
        arquivo = pd.read_json(json)
        return arquivo.to_csv()



vamoai = ViaCEP().retorna_json(ViaCEP().chamar_enderenco("PB","João Pessoa","Ana de fatima gama cabral"))
vamoai2 = ViaCEP().retorna_csv(vamoai)

print(vamoai2)


