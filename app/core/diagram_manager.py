"""
Central diagram manager.
"""
import os
import yaml
import graphviz
import re
from typing import Dict, Any, Tuple, Optional

from config.settings import UPLOAD_FOLDER
from core.diagram_generators import DIAGRAM_GENERATORS
from core.language_utils import detect_language, get_diagram_generators

def generate_diagram(yaml_data: str, filename: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """
    Process YAML data and generate the corresponding diagram.
    
    Args:
        yaml_data: YAML content as string
        filename: Name of the file to save the result
        
    Returns:
        Tuple containing (image_path, alternative_description, error)
    """
    try:
        # Load and validate YAML
        data = yaml.safe_load(yaml_data)
        
        # Check if we're dealing with English or Portuguese format
        language = detect_language(data)
        generators = get_diagram_generators(language)
        
        # Extract appropriate keys based on detected language
        if language == 'en':
            if not data or 'diagram' not in data:
                return None, None, "Error: Invalid YAML or missing 'diagram' key."
            diagram_data = data['diagram']
            diagram_type = diagram_data['type']
            diagram_title = diagram_data['title']
            alt_description = diagram_data.get(
                'alternative_description', 
                f'Diagram of type {diagram_type}'
            )
        else:  # Portuguese
            if not data or 'diagrama' not in data:
                return None, None, "Erro: YAML inválido ou chave 'diagrama' ausente."
            diagram_data = data['diagrama']
            diagram_type = diagram_data['tipo']
            diagram_title = diagram_data['titulo']
            alt_description = diagram_data.get(
                'descricao_alternativa', 
                f'Diagrama do tipo {diagram_type}'
            )

        # Select appropriate generator
        diagram_generator = generators.get(diagram_type)
        if not diagram_generator:
            error_msg = f"Diagram type '{diagram_type}' not supported." if language == 'en' else f"Tipo de diagrama '{diagram_type}' não suportado."
            return None, None, error_msg
        
        # Generate diagram
        dot = diagram_generator(diagram_data, language)
        if not dot:
            error_msg = "Error generating diagram." if language == 'en' else "Erro ao gerar diagrama."
            return None, None, error_msg

        # Render and save
        image_path = os.path.join(UPLOAD_FOLDER, f"{filename}.png")
        dot.render(os.path.splitext(image_path)[0], format="png", cleanup=True)
        
        return f"/{image_path}", alt_description, None

    except yaml.YAMLError as e:
        return None, None, f"Error loading YAML: {e}"
    except graphviz.ExecutableNotFound:
        return None, None, "Error: Graphviz is not installed or not in PATH."
    except Exception as e:
        return None, None, f"Unexpected error: {str(e)}"