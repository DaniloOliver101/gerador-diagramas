import os
from core.diagrama_base import carregar_dados_yaml, salvar_diagrama
from core.diagrama_casos_uso import gerar_diagrama_casos_de_uso
from core.diagrama_classes import gerar_diagrama_classes
from core.diagrama_sequencia import gerar_diagrama_sequencia
from core.diagrama_componentes import gerar_diagrama_componentes
from core.diagrama_implantacao import gerar_diagrama_implantacao
from core.diagrama_arquitetura import gerar_diagrama_arquitetura

def gerar_diagrama(arquivo_yaml, pasta_saida="diagramas"):
    """
    Gera um diagrama a partir de um arquivo YAML e cria um arquivo de texto com a descrição alternativa.

    Args:
        arquivo_yaml (str): Caminho para o arquivo YAML de entrada.
        pasta_saida (str): Nome da pasta onde os arquivos serão salvos.
    """
    dados = carregar_dados_yaml(arquivo_yaml)
    
    if not dados or 'diagrama' not in dados:
        print(f"Erro: Arquivo YAML '{arquivo_yaml}' não contém a chave 'diagrama' ou está vazio.")
        return

    diagrama_dados = dados['diagrama']
    tipo_diagrama = diagrama_dados['tipo']
    titulo_diagrama = diagrama_dados['titulo']
    descricao_alternativa = diagrama_dados.get('descricao_alternativa', f'Diagrama do tipo {tipo_diagrama}')

    # Criar pasta de saída se não existir
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    nome_arquivo_saida = os.path.splitext(os.path.basename(arquivo_yaml))[0]
    caminho_arquivo_saida = os.path.join(pasta_saida, nome_arquivo_saida)

    dot = None

    # Seleciona o tipo de diagrama a ser gerado
    if tipo_diagrama == "casos de uso":
        dot = gerar_diagrama_casos_de_uso(diagrama_dados)
    elif tipo_diagrama == "classes":
        dot = gerar_diagrama_classes(diagrama_dados)
    elif tipo_diagrama == "sequencia":
        dot = gerar_diagrama_sequencia(diagrama_dados)
    elif tipo_diagrama == "componentes":
        dot = gerar_diagrama_componentes(diagrama_dados)
    elif tipo_diagrama == "implantacao":
        dot = gerar_diagrama_implantacao(diagrama_dados)
    elif tipo_diagrama == "arquitetura":
        dot = gerar_diagrama_arquitetura(diagrama_dados)
    else:
        print(f"Tipo de diagrama '{tipo_diagrama}' não suportado.")
        return

    if dot:
        salvar_diagrama(dot, caminho_arquivo_saida, titulo_diagrama, descricao_alternativa)

if __name__ == "__main__":
    arquivos_yaml = [
        "casos_de_uso.yaml", 
        "classes.yaml", 
        "sequencia.yaml", 
        "componentes.yaml", 
        "implantacao.yaml",
        "arquitetura.yaml"  # Adicione um arquivo de exemplo para o novo tipo
    ]
    for arquivo in arquivos_yaml:
        gerar_diagrama(arquivo)