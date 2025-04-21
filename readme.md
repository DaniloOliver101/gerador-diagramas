# 🧩 Gerador de Diagramas

Uma aplicação web para geração de diagramas a partir de descrições YAML, com capacidade de geração de YAML através de inteligência artificial!

## ✨ Recursos

- **Geração de Diagramas**: Transforme código YAML em diagramas visuais
- **Assistente de IA**: Descreva seu diagrama em texto natural e deixe a IA gerar o YAML
- **Múltiplos Tipos de Diagramas**:
  - Casos de Uso
  - Classes
  - Sequência
  - Componentes
  - Implantação
  - Arquitetura
- **Funcionalidades Úteis**:
  - Download dos diagramas gerados
  - Descrições alternativas para acessibilidade
- **Suporte Multilíngue**: Interface e geração em Português e Inglês

## 🚀 Execução Rápida com Docker

Execute o projeto facilmente com Docker, já incluindo todas as dependências necessárias (como o Graphviz).

### ✅ Pré-requisitos

- [Docker instalado](https://docs.docker.com/get-docker/)
- Chave de API da OpenAI (para recursos de IA)

### 📦 Passos

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/DaniloOliver101/gerador-diagramas.git
   cd gerador-diagramas
   ```

2. **Configure a API da OpenAI:**
   
   Copie o arquivo de exemplo de configuração:
   ```bash
   cp app/.env.example app/.env
   ```
   
   Edite o arquivo `app/.env` e adicione sua chave de API OpenAI:
   ```
   OPENAI_API_KEY=sua-chave-da-openai-aqui
   ```

3. **Construa a imagem Docker:**

   ```bash
   docker build -t gerador-diagramas:latest app/
   ```

4. **Inicie o container:**

   ```bash
   docker run -d -p 5000:5000 -v $(pwd)/app/.env:/app/.env --name gerador-diagramas-app gerador-diagramas:latest
   ```

5. **Acesse a aplicação:**

   Abra seu navegador em: [http://localhost:5000](http://localhost:5000)

### 🛠 Gerenciamento do Container

- Ver logs:
  ```bash
  docker logs gerador-diagramas-app
  ```
- Parar:
  ```bash
  docker stop gerador-diagramas-app
  ```
- Iniciar:
  ```bash
  docker start gerador-diagramas-app
  ```
- Remover container:
  ```bash
  docker stop gerador-diagramas-app && docker rm gerador-diagramas-app
  ```
- Remover imagem:
  ```bash
  docker rmi gerador-diagramas:latest
  ```

## 🐍 Instalação Manual

### ✅ Pré-requisitos

- Python 3.9+ (verifique com `python --version`)
- pip (geralmente já vem com o Python)
- Graphviz (visualizador de grafos)

### 📥 Instalando o Graphviz

- **Windows:**  
  Baixe de [https://graphviz.org/download/](https://graphviz.org/download/), instale e adicione o diretório `bin` ao PATH. Reinicie o terminal.

- **macOS:**
  ```bash
  brew install graphviz
  ```

- **Linux (Debian/Ubuntu):**
  ```bash
  sudo apt-get install graphviz
  ```

### ⚙️ Instalando o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/DaniloOliver101/gerador-diagramas.git
   cd gerador-diagramas
   ```

2. **Crie e ative um ambiente virtual:**

   - Linux/macOS:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

   - Windows:
     ```bash
     python -m venv .venv
     .\.venv\Scripts\activate
     ```

3. **Instale as dependências:**
   ```bash
   cd app
   pip install -r requirements.txt
   ```

4. **Configure a API da OpenAI:**
   
   Copie o arquivo de exemplo de configuração:
   ```bash
   cp .env.example .env
   ```
   
   Edite o arquivo `.env` e adicione sua chave de API OpenAI:
   ```
   OPENAI_API_KEY=sua-chave-da-openai-aqui
   ```

5. **Execute a aplicação:**
   ```bash
   python app.py
   ```

6. **Acesse a aplicação:**

   Abra seu navegador em: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## 🧪 Como Usar

### Geração com IA

1. Acesse a interface web da aplicação
2. Descreva o diagrama que deseja criar na área "Generate YAML with AI"
   - Por exemplo: "Criar um diagrama de arquitetura para um sistema e-commerce com frontend, backend e banco de dados"
3. Clique em "Generate YAML with AI"
4. Revise e edite o YAML gerado, se necessário
5. Clique em "Generate Diagram" para criar o diagrama visual

### Geração Manual

1. Acesse a interface web da aplicação
2. Escreva ou cole seu código YAML na área "Edit YAML"
3. Clique em "Generate Diagram" para criar o diagrama visual

## 📂 Exemplos YAML

Veja a pasta `templates/` para exemplos prontos para:

- Casos de uso
- Diagrama de classes
- Sequência
- Componentes
- Implantação
- Arquitetura

### Exemplo de YAML para Diagrama de Arquitetura

```yaml
diagrama:
  tipo: "arquitetura"
  titulo: "Arquitetura do Sistema E-commerce"
  descricao_alternativa: "Diagrama de arquitetura para sistema de e-commerce."
  usuarios:
    - nome: "Cliente"
    - nome: "Administrador"
  servicos:
    - nome: "Frontend"
    - nome: "API Gateway"
    - nome: "Serviço de Produtos"
    - nome: "Serviço de Pedidos"
    - nome: "Banco de Dados"
  conexoes:
    - de: "Cliente"
      para: "Frontend"
      evento: "Acessa"
    - de: "Administrador"
      para: "Frontend"
      evento: "Gerencia"
    - de: "Frontend"
      para: "API Gateway"
      evento: "HTTP/REST"
    - de: "API Gateway"
      para: "Serviço de Produtos"
      evento: "HTTP/REST"
    - de: "API Gateway"
      para: "Serviço de Pedidos"
      evento: "HTTP/REST"
    - de: "Serviço de Produtos"
      para: "Banco de Dados"
      evento: "SQL"
    - de: "Serviço de Pedidos"
      para: "Banco de Dados"
      evento: "SQL"
```

## 🧯 Solução de Problemas

### Verificando a conexão com a API da OpenAI

Se os recursos de IA não estiverem funcionando, você pode testar sua chave de API executando:

```bash
python test_openai.py
```

### Problemas com Docker

- **Página não carrega?** Verifique se a porta 5000 não está em uso:
  ```bash
  docker run -d -p 8080:5000 --name gerador-diagramas-app gerador-diagramas:latest
  ```
  E acesse: [http://localhost:8080](http://localhost:8080)

- **Erro ao montar volume?** No Windows, use caminho absoluto:
  ```bash
  docker run -d -p 5000:5000 -v C:\caminho\para\.env:/app/.env --name gerador-diagramas-app gerador-diagramas:latest
  ```

### Aplicação sem Docker

- **Erro "Graphviz executável não encontrado"**: Verifique se o Graphviz está instalado e no PATH do sistema
- **Recursos de IA desabilitados**: Verifique se a variável OPENAI_API_KEY está configurada corretamente no arquivo .env

## 📚 Recursos de Aprendizado

- [Documentação do Graphviz](https://www.graphviz.org/documentation/)
- [UML - Linguagem de Modelagem Unificada](https://www.uml.org)
- [API OpenAI](https://platform.openai.com/docs/api-reference)

## 🤝 Contribuição

Pull requests são bem-vindos! Sinta-se à vontade para sugerir melhorias, corrigir bugs ou adicionar novos recursos.


