"""
AI service for generating YAML diagrams from text descriptions.
"""
import os
from typing import Optional
import openai
from config.settings import OPENAI_API_KEY
import re

# Use basic API key setup instead of client initialization
openai.api_key = OPENAI_API_KEY

def generate_yaml_from_prompt(prompt: str) -> str:
    """
    Generate a YAML diagram from a text description.
    
    Args:
        prompt (str): Description of the desired diagram
        
    Returns:
        str: Generated YAML
    """
    # Detect if the prompt is in Portuguese
    language = detect_prompt_language(prompt)
    
    # Build complete prompt for API based on language
    complete_prompt = _build_yaml_generation_prompt(prompt, language)
    
    # Send to OpenAI and clean response
    yaml_response = _send_request_to_openai(complete_prompt)
    clean_yaml = _clean_yaml_response(yaml_response)
    
    return clean_yaml

def detect_prompt_language(prompt: str) -> str:
    """
    Detect if the prompt is in Portuguese or English.
    Simple heuristic: if it has more Portuguese keywords than English ones.
    
    Args:
        prompt: The prompt to analyze
        
    Returns:
        'pt' for Portuguese, 'en' for English
    """
    # Simplified language detection - count common Portuguese words
    pt_keywords = ['diagrama', 'sistema', 'serviço', 'usuário', 'aplicação', 'conexão', 
                   'banco de dados', 'relacionamento', 'gerar', 'criar']
    
    pt_count = sum(1 for word in pt_keywords if word.lower() in prompt.lower())
    
    # If we have significant Portuguese words, assume Portuguese
    if pt_count >= 3 or 'diagrama' in prompt.lower():
        return 'pt'
    
    return 'en'

def _send_request_to_openai(prompt: str) -> str:
    """
    Send a request to OpenAI API and get the response.
    
    Args:
        prompt (str): The prompt to send to OpenAI
        
    Returns:
        str: The response from OpenAI
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates YAML diagrams."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error communicating with OpenAI: {str(e)}")

def _build_yaml_generation_prompt(user_prompt: str, language: str = 'en') -> str:
    """
    Build a complete prompt for the AI to generate diagram YAML.
    
    Args:
        user_prompt (str): The user's description of the desired diagram
        language (str): The language to use ('en' for English, 'pt' for Portuguese)
        
    Returns:
        str: Complete prompt for AI
    """
    if language == 'pt':
        return f"""
        Crie um arquivo YAML para gerar um diagrama baseado na seguinte descrição:
        
        {user_prompt}
        
        O YAML deve seguir este formato:
        
        ```yaml
        diagrama:
          tipo: [casos de uso | classes | sequencia | componentes | implantacao | arquitetura]
          titulo: [Título descritivo do diagrama]
          descricao_alternativa: [Descrição para acessibilidade]
          
          # Campos específicos para o tipo escolhido
          # Para diagramas de arquitetura, por exemplo:
          usuarios:
            - nome: [nome do usuário/ator]
          servicos:
            - nome: [nome do serviço/componente]
          conexoes:
            - de: [origem]
              para: [destino]
              evento: [descrição do fluxo]
        ```
        
        Escolha o tipo de diagrama mais apropriado para a descrição fornecida entre os tipos disponíveis.
        Forneça apenas o código YAML, sem explicações adicionais.
        """
    else:
        return f"""
        Create a YAML file to generate a diagram based on the following description:
        
        {user_prompt}
        
        The YAML should follow this format:
        
        ```yaml
        diagram:
          type: [use cases | classes | sequence | components | deployment | architecture]
          title: [Descriptive title of the diagram]
          alternative_description: [Description for accessibility]
          
          # Fields specific to the chosen type
          # For architecture diagrams, for example:
          users:
            - name: [user/actor name]
          services:
            - name: [service/component name]
          connections:
            - from: [source]
              to: [destination]
              event: [flow description]
        ```
        
        Choose the most appropriate diagram type for the provided description among the available types.
        Provide only the YAML code, without additional explanations.
        """

def _clean_yaml_response(yaml_response: str) -> str:
    """
    Clean the YAML response by removing code markers if present.
    
    Args:
        yaml_response (str): Raw response from OpenAI
        
    Returns:
        str: Cleaned YAML string
    """
    return yaml_response.replace("```yaml", "").replace("```", "").strip()