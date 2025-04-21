"""
Utilities for language detection and multi-language support.
"""
from typing import Dict, Any, Callable

# Portuguese keywords that indicate the YAML is in Portuguese
PORTUGUESE_KEYWORDS = [
    'diagrama', 'tipo', 'titulo', 'descricao_alternativa', 
    'atores', 'casos_de_uso', 'relacionamentos', 
    'classes', 'atributos', 'metodos',
    'objetos', 'mensagens', 
    'componentes', 
    'nos', 'conexoes',
    'usuarios', 'servicos'
]

def detect_language(data: Dict[str, Any]) -> str:
    """
    Detect if the YAML is in English or Portuguese.
    
    Args:
        data: Loaded YAML data
        
    Returns:
        'en' for English, 'pt' for Portuguese
    """
    # Check for Portuguese structure
    if 'diagrama' in data:
        return 'pt'
    
    # If it has the English key, it's in English
    if 'diagram' in data:
        return 'en'
    
    # Default to English if we can't determine
    return 'en'

def get_diagram_generators(language: str) -> Dict[str, Callable]:
    """
    Get the appropriate diagram generators based on language.
    
    Args:
        language: 'en' for English, 'pt' for Portuguese
        
    Returns:
        Dictionary mapping diagram types to generator functions
    """
    from core.diagram_generators import DIAGRAM_GENERATORS, PT_DIAGRAM_GENERATORS
    
    if language == 'pt':
        return PT_DIAGRAM_GENERATORS
    
    # Default to English
    return DIAGRAM_GENERATORS
