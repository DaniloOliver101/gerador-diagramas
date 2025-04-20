import graphviz

def gerar_diagrama_arquitetura(dados):
    """
    Gera um diagrama de arquitetura usando Graphviz.
    
    Args:
        dados (dict): Dados para o diagrama
        
    Returns:
        graphviz.Digraph: Objeto do diagrama
    """
    dot = graphviz.Digraph(comment=dados['titulo'], graph_attr={'rankdir': 'LR'})

    # Criar nós para usuários
    for user in dados.get('usuarios', []):
        dot.node(user['nome'], shape='oval', style='filled', fillcolor='lightgray')

    # Criar nós para serviços
    for service in dados.get('servicos', []):
        dot.node(service['nome'], shape='box', style='filled', fillcolor='lightblue')

    # Criar conexões (arestas)
    for conexao in dados.get('conexoes', []):
        dot.edge(conexao['de'], conexao['para'], label=conexao.get('evento', ''))

    return dot