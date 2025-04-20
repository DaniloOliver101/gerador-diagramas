import graphviz

def gerar_diagrama_implantacao(dados):
    """
    Gera um diagrama de implantação usando Graphviz.
    
    Args:
        dados (dict): Dados para o diagrama
        
    Returns:
        graphviz.Digraph: Objeto do diagrama
    """
    dot = graphviz.Digraph(comment=dados['titulo'], graph_attr={'rankdir': 'LR'})

    for no in dados.get('nos', []):
        if no['tipo'] == 'nó':
            dot.node(no['nome'], shape='box', style='filled', fillcolor='lightgreen')
        elif no['tipo'] == 'dispositivo':
            dot.node(no['nome'], shape='cylinder', style='filled', fillcolor='moccasin')
        elif no['tipo'] == 'banco de dados':
            dot.node(no['nome'], shape='cylinder', style='filled', fillcolor='lightyellow')
        elif no['tipo'] == 'artefato':
            dot.node(no['nome'], shape='rectangle', style='filled', fillcolor='lavender')
        if no.get('container'):
            dot.edge(no['container'], no['nome'], style='dashed')

    for conexao in dados.get('conexoes', []):
        dot.edge(conexao['de'], conexao['para'], label=conexao.get('nome', ''), arrowhead='normal')

    return dot