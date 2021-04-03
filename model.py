import requests

class Endereco:
    def __init__(self):
        self.url = "https://viacep.com.br/ws"

    def request_by_endereco(self, estado, cidade, rua):
        return requests.get(f"{self.url}/{estado}/{cidade}/{rua}/json").json()

    def request_by_cep(self, cep):
        return requests.get(f"{self.url}/{cep}/json").json()

class Estados:
    def __init__(self):
        self.url = "https://github.com/felipefdl/cidades-estados-brasil-json/raw/master/Estados.json"

    def get_id(self, sigla_estado):
        estados = requests.get(self.url).json()
        
        for dic in estados:
            if dic["Sigla"] == sigla_estado:
        
                return dic["ID"]

    def get_all(self):
        estados = requests.get(self.url).json()
        
        return [{"label": i["Nome"], "value": i["Sigla"]} for i in estados]

class Cidades:
    def __init__(self):
        self.url = "https://github.com/felipefdl/cidades-estados-brasil-json/raw/master/Cidades.json"

    def get_cidade_from_estadoid(self, estado_id):

        cidades = requests.get(self.url).json()
        return [{"label": i["Nome"], "value": i["Nome"]} for i in cidades if i["Estado"] == estado_id]

class Mapa:
    def __init__(self, cep):
        self.cep = cep
        self.url = f"https://www.google.com.br/maps?q={cep[:5]}-{cep[5:]},%20Brasil&output=embed"

    