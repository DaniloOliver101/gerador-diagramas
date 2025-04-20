import graphviz

def gerar_diagrama_classes(dados):
    """
    Gera um diagrama de classes usando Graphviz.
    
    Args:
        dados (dict): Dados para o diagrama
        
    Returns:
        graphviz.Digraph: Objeto do diagrama
    """
    dot = graphviz.Digraph(comment=dados['titulo'], graph_attr={'rankdir': 'BT'})

    for classe in dados.get('classes', []):
        nome_classe = classe['nome']
        label = f"<<table border='0' cellborder='1' cellspacing='0'><tr><td bgcolor='lightgrey'><b>{nome_classe}</b></td></tr>"
        if 'atributos' in classe:
            for atributo in classe['atributos']:
                label += f"<tr><td align='left'>{atributo}</td></tr>"
        if 'metodos' in classe:
            for metodo in classe['metodos']:
                label += f"<tr><td align='left'>{metodo}</td></tr>"
        label += "</table>>"
        dot.node(nome_classe, label=label, shape='none')

    for relacionamento in dados.get('relacionamentos', []):
        dot.edge(relacionamento['de'], relacionamento['para'], label=relacionamento.get('tipo', ''),
                 arrowhead='normal', arrowtail='none',
                 xlabel=relacionamento.get('multiplicidade_de', ''),
                 ylabel=relacionamento.get('multiplicidade_para', ''))

    return dot