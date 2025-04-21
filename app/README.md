# Diagram Generator

A web application that generates diagrams from YAML descriptions, with AI-powered YAML generation capabilities.

## Features

- Generate diagrams from YAML descriptions
- AI-powered YAML generation from text descriptions
- Support for multiple diagram types:
  - Use Case Diagrams
  - Class Diagrams
  - Sequence Diagrams
  - Component Diagrams
  - Deployment Diagrams
  - Architecture Diagrams
- Download generated diagrams
- Copy diagrams to clipboard

## Requirements

- Python 3.8+
- Graphviz
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/diagram-generator.git
cd diagram-generator
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Graphviz:
- On Ubuntu/Debian: `sudo apt-get install graphviz`
- On macOS: `brew install graphviz`
- On Windows: Download from [Graphviz website](https://graphviz.org/download/)

5. Set up environment variables:
```bash
export OPENAI_API_KEY='your-api-key-here'
export SECRET_KEY='your-secret-key-here'
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your browser and navigate to `http://localhost:5000`

3. You can either:
   - Describe your diagram in natural language and let the AI generate the YAML
   - Write your own YAML description
   - Edit the AI-generated YAML

4. Click "Generate Diagram" to create the diagram

5. Download or copy the generated diagram

## YAML Format

The YAML should follow this structure:

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

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 