# 🧩 Gerador de Diagramas

Gere diagramas diretamente a partir de arquivos YAML! Suporte para:

- Casos de Uso
- Classes
- Sequência
- Componentes
- Implantação

## 🚀 Execução Rápida com Docker

Execute o projeto facilmente com Docker, já incluindo todas as dependências necessárias (como o Graphviz).

### ✅ Pré-requisitos

- [Docker instalado](https://docs.docker.com/get-docker/)

### 📦 Passos

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/DaniloOliver101/gerador-diagramas.git
   cd gerador-diagramas
   ```

2. **Construa a imagem Docker:**

   ```bash
   docker build -t gerador-diagramas:latest .
   ```

3. **Inicie o container:**

   ```bash
   docker run -d -p 5000:5000 --name gerador-diagramas-app gerador-diagramas:latest
   ```

4. **Acesse a aplicação:**

   Abra seu navegador em: [http://localhost:5000](http://localhost:5000)

---

### 🛠 Gerenciamento do Container (Opcional)

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

---

### 🧯 Solução de Problemas Comuns

- **Página não carrega?** Verifique os logs:
  ```bash
  docker logs gerador-diagramas-app
  ```

- **Erro `ERR_EMPTY_RESPONSE`?** Verifique se o Flask está configurado para aceitar conexões externas:
  ```python
  app.run(host='0.0.0.0')
  ```

- **Porta em uso?** Use outra porta:
  ```bash
  docker run -d -p 8080:5000 gerador-diagramas:latest
  ```
  E acesse: [http://localhost:8080](http://localhost:8080)

---

## 🐍 Instalação Manual (Alternativa ao Docker)

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
   git clone https://github.com/seu-usuario/gerador-diagramas.git
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
   pip install -r requirements.txt
   ```

---

## 🧪 Como Usar

1. Crie um arquivo `.yaml` definindo seu diagrama (veja exemplos na pasta `templates_yaml`).
2. Execute o script:
   ```bash
   python app.py
   ```
3. Acesse: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
4. Cole o conteúdo do YAML, clique em **Gerar Diagrama** e visualize o resultado!

---

## 📂 Exemplos YAML

Veja a pasta `templates_yaml/` para exemplos prontos para:

- Casos de uso
- Diagrama de classes
- Sequência
- Componentes
- Implantação

---

## 🤝 Contribuição

Pull requests são bem-vindos! Sinta-se à vontade para sugerir melhorias, corrigir bugs ou adicionar novos recursos.


