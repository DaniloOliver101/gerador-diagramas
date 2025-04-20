import os
import yaml
import graphviz

def carregar_dados_yaml(arquivo_yaml):
    """
    Carrega os dados de um arquivo YAML.
    
    Args:
        arquivo_yaml (str): Caminho para o arquivo YAML.
        
    Returns:
        dict: Dados carregados ou None se ocorrer um erro.
    """
    try:
        with open(arquivo_yaml, 'r') as arquivo:
            dados = yaml.safe_load(arquivo)
        return dados
    except FileNotFoundError:
        print(f"Erro: Arquivo YAML '{arquivo_yaml}' não encontrado.")
        return None
    except yaml.YAMLError as e:
        print(f"Erro ao carregar arquivo YAML '{arquivo_yaml}': {e}")
        return None

def salvar_diagrama(dot, caminho_arquivo_saida, titulo_diagrama, descricao_alternativa):
    """
    Salva um diagrama em formato PNG e sua descrição alternativa em TXT.
    
    Args:
        dot: Objeto graphviz.Digraph com o diagrama
        caminho_arquivo_saida (str): Caminho para o arquivo de saída (sem extensão)
        titulo_diagrama (str): Título do diagrama
        descricao_alternativa (str): Descrição alternativa do diagrama
    """
    try:
        dot.render(caminho_arquivo_saida, format="png", cleanup=True)
        print(f"Diagrama '{titulo_diagrama}' gerado em: {caminho_arquivo_saida}.png")

        # Criar arquivo de texto com a descrição alternativa
        with open(f"{caminho_arquivo_saida}.txt", 'w') as arquivo_texto:
            arquivo_texto.write(f"Descrição Alternativa: {descricao_alternativa}")
        print(f"Descrição alternativa salva em: {caminho_arquivo_saida}.txt")
    except graphviz.ExecutableNotFound:
        print("Erro: Graphviz não está instalado ou não está no PATH.")
    except graphviz.FormatNotFound as e:
        print(f"Erro ao gerar o diagrama: {e}")