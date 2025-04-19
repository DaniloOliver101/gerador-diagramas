# Gerador de Diagramas

Este projeto permite gerar diagramas a partir de arquivos YAML. Ele suporta os seguintes tipos de diagramas:

* Casos de Uso
* Classes
* Sequência
* Componentes
* Implantação

## Pré-requisitos

Antes de instalar e executar o gerador de diagramas, certifique-se de que os seguintes pré-requisitos estejam instalados no seu sistema:

* **Python:** Versão 3.9 ou superior. Você pode verificar a versão instalada executando `python --version` ou `python3 --version` no terminal.
* **pip:** Gerenciador de pacotes do Python. Geralmente, o pip é instalado junto com o Python.
* **Graphviz:** Software de visualização de grafos. É necessário para gerar as imagens dos diagramas.

### Instalação do Graphviz

A instalação do Graphviz varia dependendo do sistema operacional:

* **Windows:**
    1.  Baixe o instalador do Graphviz do site oficial: [https://graphviz.org/download/](https://graphviz.org/download/)
    2.  Execute o instalador e siga as instruções.
    3.  Adicione o diretório `bin` do Graphviz (por exemplo, `C:\Program Files\Graphviz\bin`) à variável de ambiente `PATH`. Você pode fazer isso nas configurações do sistema.
    4.  Reinicie o terminal ou o computador para que a alteração na variável `PATH` seja reconhecida.
* **macOS:**
    1.  Instale o Homebrew (se ainda não estiver instalado): `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
    2.  Instale o Graphviz usando o Homebrew: `brew install graphviz`
* **Linux (Debian/Ubuntu):**
    1.  Abra o terminal.
    2.  Execute o seguinte comando: `sudo apt-get install graphviz`

## Instalação do Projeto

1.  Clone o repositório do projeto para o seu computador.
2.  Navegue até o diretório do projeto no terminal.
3.  Crie um ambiente virtual (recomendado):
    * `python3 -m venv .venv` (ou `python -m venv .venv`)
    * Ative o ambiente virtual:
        * **Linux/macOS:** `source .venv/bin/activate`
        * **Windows:** `.\.venv\Scripts\activate`
4.  Instale as dependências do Python: `pip install -r requirements.txt`

## Uso

1.  Crie um arquivo YAML com a definição do diagrama que você deseja gerar. Você pode usar os templates fornecidos como referência.
2.  Execute o script principal: `python app.py`
3.  Abra o navegador e acesse `http://127.0.0.1:5000/`.
4.  Cole o conteúdo do arquivo YAML no campo de texto e clique no botão "Gerar Diagrama".
5.  O diagrama será exibido na página, juntamente com as opções para download e cópia.

## Exemplos de Arquivos YAML

Consulte a pasta `templates_yaml` para exemplos de arquivos YAML para cada tipo de diagrama.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou novos recursos.

## Licença

[Especificar a licença do projeto]