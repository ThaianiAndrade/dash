# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

#
# 1 - INICIANDO APLICAÇÃO
#
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

#
# 2 - DEMONSTRATIVO DE BANCO DE DADOS
#

df = pd.read_excel("C:\\Users\\thaia\\Projetos\\dash\\dash\\dashboard\\Vendas.xlsx") # base de dados vinda de um excel

#
# 3 - CRIANDO O GRÁFICO
#
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group") # criacao do grafico. Linha: Produto, Coluna: Quantidade, Cor: Loja
opcoes = list(df['ID Loja'].unique()) # lista com as lojas (selectbox)
opcoes.append('Todas as Lojas') # adiciona na lista a opção Todas as Lojas

#
# 4 - CRIANDO O LAYOUT
#
app.layout = html.Div(children=[
    html.H1(children='iReposição'),

    html.Div(children='''
       Painel de solicitação de reposição de produtos.
    '''),
    
    html.H2(children='Entidade Matriz'),
    dcc.Dropdown(opcoes, value='Todas as Lojas', id='lista_lojas'),
    dcc.Graph(
        id='grafico_quantidade_vendas',
        figure=fig
    )
])

#
# 5 - DECORATOR
#
@app.callback(
    Output('grafico_quantidade_vendas', 'figure'), # quem vai ser editado
    Input('lista_lojas', 'value') # quem vai editar
)
def update_output(value): # se tiver selecionada 1 loja, vai exibir o grafico dessa loja, se tiver selecionada Todas as Lojas, vai mostrar o grafico geral de todas as lojas.
    if value == 'Todas as Lojas':
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Loja'] == value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
