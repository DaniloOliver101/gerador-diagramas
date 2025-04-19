import yaml
import graphviz
import os

def gerar_diagrama(arquivo_yaml, pasta_saida="diagramas"):
    """
    Gera um diagrama a partir de um arquivo YAML e cria um arquivo de texto com a descrição alternativa.

    Args:
        arquivo_yaml (str): Caminho para o arquivo YAML de entrada.
        pasta_saida (str): Nome da pasta onde os arquivos serão salvos.
    """

    try:
        with open(arquivo_yaml, 'r') as arquivo:
            dados = yaml.safe_load(arquivo)
    except FileNotFoundError:
        print(f"Erro: Arquivo YAML '{arquivo_yaml}' não encontrado.")
        return
    except yaml.YAMLError as e:
        print(f"Erro ao carregar arquivo YAML '{arquivo_yaml}': {e}")
        return

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
    else:
        print(f"Tipo de diagrama '{tipo_diagrama}' não suportado.")
        return

    if dot:
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

def gerar_diagrama_casos_de_uso(dados):
    dot = graphviz.Digraph(comment=dados['titulo'], graph_attr={'rankdir': 'LR'})
    for ator in dados.get('atores', []):
        dot.node(ator['nome'], shape='oval')  # 'actor' -> 'oval'
    for caso_de_uso in dados.get('casos_de_uso', []):
        dot.node(caso_de_uso['nome'], shape='ellipse')
    for relacionamento in dados.get('relacionamentos', []):
        dot.edge(relacionamento['de'], relacionamento['para'], label=relacionamento.get('tipo', ''))
    return dot

def gerar_diagrama_classes(dados):
    dot = graphviz.Digraph(comment=dados['titulo'], graph_attr={'rankdir': 'BT'})

    for classe in dados.get('classes', []):
        nome_classe = classe['nome']
        label = f"<<table border='0' cellborder='1' cellspacing='0'><tr><td bgcolor='lightgrey'><b>{nome_classe}</b></td></tr>"
        if 'atributos' in classe:
            for atributo in classe['atributos']:
                label += f"<tr><td align='left'>{atributo}</td></tr>"
        if 'metodos' in classe:
            for metodo in classe['metodos']:
                label += f"<tr><td align='left'>{metodo}</td></tr>"
        label += "</table>>"
        dot.node(nome_classe, label=label, shape='none')

    for relacionamento in dados.get('relacionamentos', []):
        dot.edge(relacionamento['de'], relacionamento['para'], label=relacionamento.get('tipo', ''),
                 arrowhead='normal', arrowtail='none',
                 xlabel=relacionamento.get('multiplicidade_de', ''),
                 ylabel=relacionamento.get('multiplicidade_para', ''))

    return dot

def gerar_diagrama_sequencia(dados):
    dot = graphviz.Digraph(comment=dados['titulo'], graph_attr={'rankdir': 'TB'})

    for objeto in dados.get('objetos', []):
        dot.node(objeto['nome'], shape='box')

    for mensagem in dados.get('mensagens', []):
        dot.edge(mensagem['de'], mensagem['para'], label=mensagem['mensagem'], arrowhead='normal')

    return dot
def gerar_diagrama_componentes(dados):
    dot = graphviz.Digraph(comment=dados['titulo'], graph_attr={'rankdir': 'LR'})

    for componente in dados.get('componentes', []):
        dot.node(componente['nome'], shape='component', style='filled', fillcolor='lightblue')

    for relacionamento in dados.get('relacionamentos', []):
        dot.edge(relacionamento['de'], relacionamento['para'], label=relacionamento['tipo'])

    return dot

def gerar_diagrama_implantacao(dados):
    dot = graphviz.Digraph(comment=dados['titulo'], graph_attr={'rankdir': 'LR'})

    for no in dados.get('nos', []):
        if no['tipo'] == 'nó':
            dot.node(no['nome'], shape='box', style='filled', fillcolor='lightgreen')
        elif no['tipo'] == 'dispositivo':
            dot.node(no['nome'], shape='cylinder', style='filled', fillcolor='moccasin')
        elif no['tipo'] == 'banco de dados':
            dot.node(no['nome'], shape='cylinder', style='filled', fillcolor='lightyellow')  # 'database' -> 'cylinder'
        elif no['tipo'] == 'artefato':
            dot.node(no['nome'], shape='rectangle', style='filled', fillcolor='lavender')
        if no.get('container'):
            dot.edge(no['container'], no['nome'], style='dashed')

    for conexao in dados.get('conexoes', []):
        dot.edge(conexao['de'], conexao['para'], label=conexao.get('nome', ''), arrowhead='normal')

    return dot

if __name__ == "__main__":
    arquivos_yaml = ["casos_de_uso.yaml", "classes.yaml", "sequencia.yaml", "componentes.yaml", "implantacao.yaml"]
    for arquivo in arquivos_yaml:
        gerar_diagrama(arquivo)