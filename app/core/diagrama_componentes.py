import graphviz

def gerar_diagrama_componentes(dados):
    """
    Gera um diagrama de componentes usando Graphviz.
    
    Args:
        dados (dict): Dados para o diagrama
        
    Returns:
        graphviz.Digraph: Objeto do diagrama
    """
    dot = graphviz.Digraph(comment=dados['titulo'], graph_attr={'rankdir': 'LR'})

    for componente in dados.get('componentes', []):
        dot.node(componente['nome'], shape='component', style='filled', fillcolor='lightblue')

    for relacionamento in dados.get('relacionamentos', []):
        dot.edge(relacionamento['de'], relacionamento['para'], label=relacionamento['tipo'])

    return dot