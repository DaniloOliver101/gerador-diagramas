"""
Gerador de diagramas de classes.
"""
import graphviz
from typing import Dict, Any


def generate_class_label(class_name: str, class_data: Dict[str, Any]) -> str:
    """
    Gera o HTML para o label de uma classe.
    
    Args:
        class_name (str): Nome da classe
        class_data (Dict[str, Any]): Dados da classe
        
    Returns:
        str: Label HTML formatado
    """
    label = f"<<table border='0' cellborder='1' cellspacing='0'><tr><td bgcolor='lightgrey'><b>{class_name}</b></td></tr>"
    
    # Atributos
    if 'atributos' in class_data:
        for attribute in class_data['atributos']:
            label += f"<tr><td align='left'>{attribute}</td></tr>"
    
    # Métodos
    if 'metodos' in class_data:
        for method in class_data['metodos']:
            label += f"<tr><td align='left'>{method}</td></tr>"
            
    label += "</table>>"
    return label


def generate_class_diagram(data: Dict[str, Any]) -> graphviz.Digraph:
    """
    Gera um diagrama de classes usando Graphviz.
    
    Args:
        data (Dict[str, Any]): Dados para o diagrama
        
    Returns:
        graphviz.Digraph: Objeto do diagrama
    """
    dot = graphviz.Digraph(comment=data['titulo'], graph_attr={'rankdir': 'BT'})

    # Criar nós para cada classe
    for class_item in data.get('classes', []):
        class_name = class_item['nome']
        label = generate_class_label(class_name, class_item)
        dot.node(class_name, label=label, shape='none')

    # Adicionar relacionamentos
    for relationship in data.get('relacionamentos', []):
        dot.edge(
            relationship['de'], 
            relationship['para'], 
            label=relationship.get('tipo', ''),
            arrowhead='normal', 
            arrowtail='none',
            xlabel=relationship.get('multiplicidade_de', ''),
            ylabel=relationship.get('multiplicidade_para', '')
        )

    return dot