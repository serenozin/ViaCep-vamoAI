import pandas as pd
from pandas.io import json
from requests.api import head
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
        if isinstance(json, list):
            json_dict = {i: json[i] for i in range(len(json))}
        else: 
            json_dict = {0: json}
        df = pd.DataFrame.from_dict(json_dict, orient='index')
        return df.to_csv()
    #bug corrigido, o isistance resolveu.
    def mapa(self):
        json = self.to_json()
        print(type(json))
        if isinstance(json, list):
            print(json[0]["cep"])
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

class Download:
    def __init__(self,json):
        self.json = pd.read_json(json)
    def generate_to_csv(self):
        return self.json.to_csv(f'endereco.csv', index=None, header = True)
    def generate_to_json(self):
        return self.json.to_json(f'endereco.json', index= None, header = True)

        
    
