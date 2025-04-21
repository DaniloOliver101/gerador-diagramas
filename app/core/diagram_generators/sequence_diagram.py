"""
Gerador de diagramas de sequência.
"""
import graphviz
from typing import Dict, Any


def generate_sequence_diagram(data: Dict[str, Any]) -> graphviz.Digraph:
    """
    Gera um diagrama de sequência usando Graphviz.
    
    Args:
        data (Dict[str, Any]): Dados para o diagrama
        
    Returns:
        graphviz.Digraph: Objeto do diagrama
    """
    dot = graphviz.Digraph(comment=data['titulo'], graph_attr={'rankdir': 'TB'})

    # Adicionar objetos
    for obj in data.get('objetos', []):
        dot.node(obj['nome'], shape='box')

    # Adicionar mensagens
    for message in data.get('mensagens', []):
        dot.edge(
            message['de'], 
            message['para'], 
            label=message['mensagem'], 
            arrowhead='normal'
        )

    return dot