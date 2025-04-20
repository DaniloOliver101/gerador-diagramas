import graphviz

def gerar_diagrama_sequencia(dados):
    """
    Gera um diagrama de sequência usando Graphviz.
    
    Args:
        dados (dict): Dados para o diagrama
        
    Returns:
        graphviz.Digraph: Objeto do diagrama
    """
    dot = graphviz.Digraph(comment=dados['titulo'], graph_attr={'rankdir': 'TB'})

    for objeto in dados.get('objetos', []):
        dot.node(objeto['nome'], shape='box')

    for mensagem in dados.get('mensagens', []):
        dot.edge(mensagem['de'], mensagem['para'], label=mensagem['mensagem'], arrowhead='normal')

    return dot