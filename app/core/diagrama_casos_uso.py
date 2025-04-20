import graphviz

def gerar_diagrama_casos_de_uso(dados):
    """
    Gera um diagrama de casos de uso usando Graphviz.
    
    Args:
        dados (dict): Dados para o diagrama
        
    Returns:
        graphviz.Digraph: Objeto do diagrama
    """
    dot = graphviz.Digraph(comment=dados['titulo'], graph_attr={'rankdir': 'LR'})
    for ator in dados.get('atores', []):
        dot.node(ator['nome'], shape='oval')
    for caso_de_uso in dados.get('casos_de_uso', []):
        dot.node(caso_de_uso['nome'], shape='ellipse')
    for relacionamento in dados.get('relacionamentos', []):
        dot.edge(relacionamento['de'], relacionamento['para'], label=relacionamento.get('tipo', ''))
    return dot