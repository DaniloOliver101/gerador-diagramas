"""
Serviço de IA para geração de diagramas YAML a partir de descrições textuais.
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
    Gera um diagrama YAML a partir de uma descrição textual.
    
    Args:
        prompt (str): Descrição do diagrama desejado
        
    Returns:
        str: YAML gerado
    """
    # Detectar se o prompt está em português
    language = detect_prompt_language(prompt)
    
    # Construir prompt completo para a API com base no idioma
    complete_prompt = _build_yaml_generation_prompt(prompt, language)
    
    # Enviar para a OpenAI e limpar resposta
    yaml_response = _send_request_to_openai(complete_prompt)
    clean_yaml = _clean_yaml_response(yaml_response)
    
    return clean_yaml

def detect_prompt_language(prompt: str) -> str:
    """
    Detecta se o prompt está em português ou inglês.
    Heurística simples: se tem mais palavras-chave em português que em inglês.
    
    Args:
        prompt: O prompt a ser analisado
        
    Returns:
        'pt' para português, 'en' para inglês
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
    Envia uma requisição para a API da OpenAI e obtém a resposta.
    
    Args:
        prompt (str): O prompt para enviar à OpenAI
        
    Returns:
        str: A resposta da OpenAI
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente útil que gera diagramas YAML."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Erro ao comunicar com a OpenAI: {str(e)}")

def _build_yaml_generation_prompt(user_prompt: str, language: str = 'en') -> str:
    """
    Constrói um prompt completo para a IA gerar YAML de diagrama.
    
    Args:
        user_prompt (str): A descrição do diagrama desejado pelo usuário
        language (str): O idioma a ser usado ('en' para inglês, 'pt' para português)
        
    Returns:
        str: Prompt completo para a IA
    """
    # Sempre usar o formato em português para o YAML de saída
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
    Mesmo que o prompt esteja em inglês, SEMPRE retorne o YAML em português brasileiro seguindo exatamente o formato acima.
    """

def _clean_yaml_response(yaml_response: str) -> str:
    """
    Limpa a resposta YAML removendo marcadores de código se presentes.
    
    Args:
        yaml_response (str): Resposta bruta da OpenAI
        
    Returns:
        str: String YAML limpa
    """
    return yaml_response.replace("```yaml", "").replace("```", "").strip()