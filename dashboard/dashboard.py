# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


#
# 1 - INICIANDO APLICAÇÃO
#
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
# import os

app = Dash(__name__)

#
# 2 - DEMONSTRATIVO DE BANCO DE DADOS
#
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

# # Imprimir o diretório de trabalho atual
# print(os.getcwd())

# # Verifique se o arquivo está realmente no diretório de trabalho atual
# print(os.listdir())

df = pd.read_excel("C:\\Users\\thaia\\Projetos\\dash\\dash\\dashboard\\Vendas.xlsx")

#
# 3 - CRIANDO O GRÁFICO
#
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")

#
# 4 - CRIANDO O LAYOUT
#
app.layout = html.Div(children=[
    html.H1(children='iReposição'),

    html.Div(children='''
       Painel de solicitação de reposição de produtos.
    '''),
    
    html.H2(children='Entidade Matriz'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)