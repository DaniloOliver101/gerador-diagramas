"""
Gerador de diagramas de casos de uso.
"""
import graphviz
from typing import Dict, Any


def generate_use_case_diagram(data: Dict[str, Any]) -> graphviz.Digraph:
    """
    Gera um diagrama de casos de uso usando Graphviz.
    
    Args:
        data (Dict[str, Any]): Dados para o diagrama
        
    Returns:
        graphviz.Digraph: Objeto do diagrama
    """
    dot = graphviz.Digraph(comment=data['titulo'], graph_attr={'rankdir': 'LR'})
    
    # Adicionar atores
    for actor in data.get('atores', []):
        dot.node(actor['nome'], shape='oval')
    
    # Adicionar casos de uso
    for use_case in data.get('casos_de_uso', []):
        dot.node(use_case['nome'], shape='ellipse')
    
    # Adicionar relacionamentos
    for relationship in data.get('relacionamentos', []):
        dot.edge(
            relationship['de'], 
            relationship['para'], 
            label=relationship.get('tipo', '')
        )
        
    return dot