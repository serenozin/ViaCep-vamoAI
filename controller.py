import pandas as pd
from model import Viacep, Cities, States, Mapa

class Andress:
    def __init__(self, uf=None, cidade=None, logradouro=None, cep=None):
        self.uf = uf 
        self.cidade = cidade
        self.logradouro = logradouro
        self.cep = cep
        self.model = Viacep(uf=uf, cidade=cidade, logradouro=logradouro, cep=cep)

    def code(self):
        return self.model.request().status_code

    def to_json(self):
        return self.model.request().json()

    def to_csv(self):
        json = self.to_json()
        if json is list:
            json_dict = {i: json[i] for i in range(len(json))}
        else: 
            json_dict = {0: json}
        df = pd.DataFrame.from_dict(json_dict, orient='index')
        return df.to_csv()

    def mapa(self):
        json = self.to_json()
        if json is list:
            return Mapa(json[0]["cep"]).request()
        else:
            return Mapa(json["cep"]).request()

class SearchOptions:
    def __init__(self):
        self.cities = Cities().request().json()
        self.states = States().request().json()

    def all_states(self):
        return [{"label": i["Nome"], "value": i["Sigla"]} for i in self.states]

    def cities_from_state(self, sigla_uf=None):
        for dic in self.states:
            if dic["Sigla"] == sigla_uf:
                id = dic["ID"]
        
        return [{"label": i["Nome"], "value": i["Nome"]} for i in self.cities if i["Estado"] == id]
