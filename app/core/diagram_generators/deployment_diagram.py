"""
Gerador de diagramas de implantação.
"""
import graphviz
from typing import Dict, Any, Tuple


def get_node_style(node_type: str) -> Dict[str, str]:
    """
    Retorna o estilo apropriado para o tipo de nó.
    
    Args:
        node_type (str): Tipo do nó
        
    Returns:
        Dict[str, str]: Atributos de estilo
    """
    styles = {
        'nó': {'shape': 'box', 'style': 'filled', 'fillcolor': 'lightgreen'},
        'dispositivo': {'shape': 'cylinder', 'style': 'filled', 'fillcolor': 'moccasin'},
        'banco de dados': {'shape': 'cylinder', 'style': 'filled', 'fillcolor': 'lightyellow'},
        'artefato': {'shape': 'rectangle', 'style': 'filled', 'fillcolor': 'lavender'}
    }
    return styles.get(node_type, {'shape': 'box'})


def generate_deployment_diagram(data: Dict[str, Any]) -> graphviz.Digraph:
    """
    Gera um diagrama de implantação usando Graphviz.
    
    Args:
        data (Dict[str, Any]): Dados para o diagrama
        
    Returns:
        graphviz.Digraph: Objeto do diagrama
    """
    dot = graphviz.Digraph(comment=data['titulo'], graph_attr={'rankdir': 'LR'})

    # Adicionar nós
    for node in data.get('nos', []):
        node_style = get_node_style(node['tipo'])
        dot.node(node['nome'], **node_style)
        
        # Adicionar relação de contêiner
        if node.get('container'):
            dot.edge(node['container'], node['nome'], style='dashed')

    # Adicionar conexões
    for connection in data.get('conexoes', []):
        dot.edge(
            connection['de'], 
            connection['para'], 
            label=connection.get('nome', ''), 
            arrowhead='normal'
        )

    return dot