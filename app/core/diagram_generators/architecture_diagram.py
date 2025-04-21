"""
Gerador de diagramas de arquitetura.
"""
import graphviz
from typing import Dict, Any


def generate_architecture_diagram(data: Dict[str, Any], language: str = 'en') -> graphviz.Digraph:
    """
    Gera um diagrama de arquitetura usando Graphviz.
    
    Args:
        data (Dict[str, Any]): Dados para o diagrama
        language (str): Idioma do diagrama ('en' para inglês, 'pt' para português)
        
    Returns:
        graphviz.Digraph: Objeto do diagrama
    """
    # Use the title field based on language
    title_field = 'title' if language == 'en' else 'titulo'
    title = data.get(title_field, 'Architecture Diagram')
    
    dot = graphviz.Digraph(comment=title, graph_attr={'rankdir': 'LR'})

    # Field names based on language
    users_field = 'users' if language == 'en' else 'usuarios'
    services_field = 'services' if language == 'en' else 'servicos'
    connections_field = 'connections' if language == 'en' else 'conexoes'
    name_field = 'name' if language == 'en' else 'nome'
    from_field = 'from' if language == 'en' else 'de'
    to_field = 'to' if language == 'en' else 'para'
    event_field = 'event' if language == 'en' else 'evento'

    # Criar nós para usuários
    for user in data.get(users_field, []):
        dot.node(
            user[name_field], 
            shape='oval', 
            style='filled', 
            fillcolor='lightgray'
        )

    # Criar nós para serviços
    for service in data.get(services_field, []):
        dot.node(
            service[name_field], 
            shape='box', 
            style='filled', 
            fillcolor='lightblue'
        )

    # Criar conexões (arestas)
    for connection in data.get(connections_field, []):
        dot.edge(
            connection[from_field], 
            connection[to_field], 
            label=connection.get(event_field, '')
        )

    return dot