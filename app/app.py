from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import uuid
import yaml
import graphviz

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'temp'  # Pasta para salvar temporariamente as imagens

# Certifique-se de que a pasta 'temp' existe
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def gerar_diagrama(yaml_data, filename):
    """
    Gera um diagrama a partir de dados YAML e salva em um arquivo.

    Args:
        yaml_data (str): Dados YAML do diagrama.
        filename (str): Nome do arquivo para salvar o diagrama.

    Returns:
        str: Caminho para o arquivo de imagem gerado.
        str: Descrição alternativa do diagrama.
        str: Erro, se ocorrer algum.
    """
    try:
        dados = yaml.safe_load(yaml_data)
        if not dados or 'diagrama' not in dados:
            return None, None, "Erro: YAML inválido ou sem a chave 'diagrama'."

        diagrama_dados = dados['diagrama']
        tipo_diagrama = diagrama_dados['tipo']
        titulo_diagrama = diagrama_dados['titulo']
        descricao_alternativa = diagrama_dados.get('descricao_alternativa', f'Diagrama do tipo {tipo_diagrama}')

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
            return None, None, f"Tipo de diagrama '{tipo_diagrama}' não suportado."

        if dot:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{filename}.png")
            dot.render(os.path.splitext(image_path)[0], format="png", cleanup=True)
            return f"/{image_path}", descricao_alternativa, None
        else:
            return None, None, "Erro ao gerar o diagrama."

    except yaml.YAMLError as e:
        return None, None, f"Erro ao carregar YAML: {e}"
    except graphviz.ExecutableNotFound:
        return None, None, "Erro: Graphviz não está instalado ou não está no PATH."
    except Exception as e:
        return None, None, f"Erro inesperado: {e}"


def gerar_diagrama_casos_de_uso(dados):
    dot = graphviz.Digraph(comment=dados['titulo'], graph_attr={'rankdir': 'LR'})
    for ator in dados.get('atores', []):
        dot.node(ator['nome'], shape='oval')
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
            dot.node(no['nome'], shape='cylinder', style='filled', fillcolor='lightyellow')
        elif no['tipo'] == 'artefato':
            dot.node(no['nome'], shape='rectangle', style='filled', fillcolor='lavender')
        if no.get('container'):
            dot.edge(no['container'], no['nome'], style='dashed')

    for conexao in dados.get('conexoes', []):
        dot.edge(conexao['de'], conexao['para'], label=conexao.get('nome', ''), arrowhead='normal')

    return dot

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar_diagrama', methods=['POST'])
def gerar_diagrama_rota():
    yaml_data = request.json['yaml_data']
    filename = str(uuid.uuid4())  # Gera um nome de arquivo único
    image_path, descricao_alternativa, erro = gerar_diagrama(yaml_data, filename)

    if erro:
        return jsonify({'erro': erro}), 400
    else:
        return jsonify({
            'imagem_path': image_path,
            'descricao_alternativa': descricao_alternativa
        })

@app.route('/temp/<filename>')
def temp_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)