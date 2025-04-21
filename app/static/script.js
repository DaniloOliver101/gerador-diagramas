/**
 * AI-powered YAML generation functionality
 */
document.getElementById('gerar-yaml').addEventListener('click', () => {
    const prompt = document.getElementById('ai-prompt').value;
    
    if (!prompt || prompt.trim().length < 10) {
        alert('Please provide a more detailed description of the desired diagram.');
        return;
    }
    
    // Show loader
    document.getElementById('ai-loader').style.display = 'block';
    
    fetchYamlFromAI(prompt);
});

/**
 * Send request to AI service to generate YAML
 * @param {string} prompt - The user's description of the desired diagram
 */
function fetchYamlFromAI(prompt) {
    fetch('/generate_yaml', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt: prompt })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Request failed');
        }
        return response.json();
    })
    .then(data => {
        // Hide loader
        document.getElementById('ai-loader').style.display = 'none';
        
        if (data.error) {
            alert("Error generating YAML: " + data.error);
        } else {
            // Fill YAML area with result
            document.getElementById('yaml-input').value = data.yaml;
        }
    })
    .catch(error => {
        // Hide loader
        document.getElementById('ai-loader').style.display = 'none';
        console.error('Request error:', error);
        alert('An error occurred while generating the YAML. Please try again later.');
    });
}

/**
 * Diagram generation functionality
 */
document.getElementById('gerar-diagrama').addEventListener('click', () => {
    const yamlInput = document.getElementById('yaml-input').value;

    if (!yamlInput || yamlInput.trim().length === 0) {
        alert('Please provide YAML code for the diagram.');
        return;
    }

    generateDiagramFromYaml(yamlInput);
});

/**
 * Send request to generate diagram from YAML
 * @param {string} yamlInput - The YAML specification for the diagram
 */
function generateDiagramFromYaml(yamlInput) {
    fetch('/generate_diagram', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ yaml_data: yamlInput })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert("Error generating diagram: " + data.error);
        } else {
            displayGeneratedDiagram(data.image_path, data.alternative_description);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while generating the diagram. Please try again later.');
    });
}

/**
 * Display the generated diagram in the UI
 * @param {string} imagePath - Path to the generated diagram image
 * @param {string} alternativeDescription - Accessibility description for the diagram
 */
function displayGeneratedDiagram(imagePath, alternativeDescription) {
    const imgElement = `<img src="${imagePath}" alt="${alternativeDescription}">`;
    document.getElementById('diagrama-container').innerHTML = imgElement;
    document.getElementById('descricao-alternativa').textContent = alternativeDescription;

    // Show download and copy buttons
    document.getElementById('download-diagram').style.display = 'inline-block';
    document.getElementById('copy-diagram').style.display = 'inline-block';

    // Configure download button
    document.getElementById('download-diagram').onclick = () => {
        const a = document.createElement('a');
        a.href = imagePath;
        a.download = 'diagram.png';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    };
}