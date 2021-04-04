import requests

class Viacep:
    def __init__(self, uf=None, cidade=None, logradouro=None, cep=None):
        self.uf = uf 
        self.cidade = cidade
        self.logradouro = logradouro
        self.cep = cep
        self.url = "https://viacep.com.br/ws"

    def request(self):
        if self.cep is None:
            return requests.get(f"{self.url}/{self.uf}/{self.cidade}/{self.logradouro}/json")
        else:
            return requests.get(f"{self.url}/{self.cep}/json")
        
class States:
    def __init__(self):
        self.url = "https://github.com/felipefdl/cidades-estados-brasil-json/raw/master/Estados.json"
        
    def request(self):
        return requests.get(self.url)

class Cities:
    def __init__(self):
        self.url = "https://github.com/felipefdl/cidades-estados-brasil-json/raw/master/Cidades.json"

    def request(self):
        return requests.get(self.url)

class Mapa:
    def __init__(self, cep):
        self.cep = cep
        
    def request(self):
        if "-" in self.cep:
            self.cep = self.cep[:5] + self.cep[6:]
        return f"https://www.google.com.br/maps?q={self.cep[:5]}-{self.cep[5:]},%20Brasil&output=embed"
