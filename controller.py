import os
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

    def response(self):
        return self.model.request()

    def as_json(self):
        return self.model.to_json()

    def mapa(self):
        json = self.as_json()

        if isinstance(json, list):
            print(json[0]["cep"])
            return Mapa(json[0]["cep"]).url()
        else:
            return Mapa(json["cep"]).url()

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
    def __init__(self, json):
        self.json = json

    def as_csv(self):
        if isinstance(self.json, list):
            json_dict = {i: self.json[i] for i in range(len(self.json))}
        else: 
            json_dict = {0: self.json}
        df = pd.DataFrame.from_dict(json_dict, orient='index')
        return df.to_csv(r"/home/serenozin/codes/Resilia/ViaCep-vamoAI/download/endereços.csv")

    def as_json(self):
        if isinstance(self.json, list):
            json_dict = {i: self.json[i] for i in range(len(self.json))}
        else: 
            json_dict = {0: self.json}
        df = pd.DataFrame.from_dict(json_dict)
        return df.to_json(r"/home/serenozin/codes/Resilia/ViaCep-vamoAI/download/endereços.json")

