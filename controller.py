from view import app
from model import Mapa

# def Incorporar(url, altura, largura):
#     return <iframe src=url width=largura height=altura>  

if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=True)  # Turn off reloader if inside Jupyter