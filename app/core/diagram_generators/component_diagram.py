"""
Gerador de diagramas de componentes.
"""
import graphviz
from typing import Dict, Any


def generate_component_diagram(data: Dict[str, Any], language: str = 'en') -> graphviz.Digraph:
    """
    Gera um diagrama de componentes usando Graphviz.
    
    Args:
        data (Dict[str, Any]): Dados para o diagrama
        language (str): Idioma do diagrama ('en' para inglês, 'pt' para português)
        
    Returns:
        graphviz.Digraph: Objeto do diagrama
    """
    # Use the title field based on language
    title_field = 'title' if language == 'en' else 'titulo'
    title = data.get(title_field, 'Component Diagram')
    
    dot = graphviz.Digraph(comment=title, graph_attr={'rankdir': 'LR'})

    # Field names based on language
    components_field = 'components' if language == 'en' else 'componentes'
    relationships_field = 'relationships' if language == 'en' else 'relacionamentos'
    name_field = 'name' if language == 'en' else 'nome'
    from_field = 'from' if language == 'en' else 'de'
    to_field = 'to' if language == 'en' else 'para'
    type_field = 'type' if language == 'en' else 'tipo'

    # Adicionar componentes
    for component in data.get(components_field, []):
        dot.node(
            component[name_field], 
            shape='component', 
            style='filled', 
            fillcolor='lightblue'
        )

    # Adicionar relacionamentos
    for relationship in data.get(relationships_field, []):
        dot.edge(
            relationship[from_field], 
            relationship[to_field], 
            label=relationship[type_field]
        )

    return dot