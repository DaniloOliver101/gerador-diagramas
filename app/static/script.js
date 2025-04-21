/**
 * Funcionalidade de geração de YAML com IA
 */
document.getElementById('gerar-yaml').addEventListener('click', () => {
    const prompt = document.getElementById('ai-prompt').value;
    
    if (!prompt || prompt.trim().length < 10) {
        showError('ai-error', 'Por favor, forneça uma descrição mais detalhada do diagrama desejado.');
        return;
    }
    
    // Mostrar loader e esconder outras mensagens de status
    showStatus('ai-loader', true);
    showStatus('ai-success', false);
    showStatus('ai-error', false);
    
    fetchYamlFromAI(prompt);
});

/**
 * Enviar solicitação ao serviço de IA para gerar YAML
 * @param {string} prompt - A descrição do usuário para o diagrama desejado
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
            // Tratamento específico para códigos de status
            if (response.status === 503) {
                throw new Error('Chave da API OpenAI não configurada. Recursos de IA indisponíveis.');
            }
            throw new Error('Falha na requisição');
        }
        return response.json();
    })
    .then(data => {
        // Esconder loader
        showStatus('ai-loader', false);
        
        if (data.error) {
            showError('ai-error', "Erro ao gerar YAML: " + data.error);
        } else {
            // Mostrar mensagem de sucesso
            showStatus('ai-success', true);
            // Preencher área YAML com resultado
            document.getElementById('yaml-input').value = data.yaml;
            
            // Anunciar para leitores de tela
            announceForScreenReader("YAML gerado com sucesso e inserido no campo de edição.");
            
            // Rolar até a área de edição de YAML
            document.getElementById('yaml-input').scrollIntoView({ behavior: 'smooth' });
            
            // Depois de um tempo, esconder a mensagem de sucesso
            setTimeout(() => {
                showStatus('ai-success', false);
            }, 3000);
        }
    })
    .catch(error => {
        // Esconder loader
        showStatus('ai-loader', false);
        console.error('Erro na requisição:', error);
        showError('ai-error', 'Ocorreu um erro: ' + error.message);
    });
}

/**
 * Funcionalidade de geração de diagrama
 */
document.getElementById('gerar-diagrama').addEventListener('click', () => {
    const yamlInput = document.getElementById('yaml-input').value;

    if (!yamlInput || yamlInput.trim().length === 0) {
        showError('diagram-error', 'Por favor, forneça o código YAML para o diagrama.');
        return;
    }

    // Mostrar loader e esconder outras mensagens de status
    showStatus('diagram-loader', true);
    showStatus('diagram-success', false);
    showStatus('diagram-error', false);
    
    generateDiagramFromYaml(yamlInput);
});

/**
 * Enviar solicitação para gerar diagrama a partir do YAML
 * @param {string} yamlInput - A especificação YAML para o diagrama
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
        // Esconder loader
        showStatus('diagram-loader', false);
        
        if (data.error) {
            showError('diagram-error', "Erro ao gerar diagrama: " + data.error);
        } else {
            // Mostrar mensagem de sucesso
            showStatus('diagram-success', true);
            displayGeneratedDiagram(data.image_path, data.alternative_description);
            
            // Depois de um tempo, esconder a mensagem de sucesso
            setTimeout(() => {
                showStatus('diagram-success', false);
            }, 3000);
        }
    })
    .catch(error => {
        // Esconder loader
        showStatus('diagram-loader', false);
        console.error('Erro:', error);
        showError('diagram-error', 'Ocorreu um erro ao gerar o diagrama. Por favor, tente novamente mais tarde.');
    });
}

/**
 * Exibir o diagrama gerado na interface
 * @param {string} imagePath - Caminho para a imagem do diagrama gerado
 * @param {string} alternativeDescription - Descrição de acessibilidade para o diagrama
 */
function displayGeneratedDiagram(imagePath, alternativeDescription) {
    const imgElement = `<img src="${imagePath}" alt="${alternativeDescription}">`;
    document.getElementById('diagrama-container').innerHTML = imgElement;
    document.getElementById('descricao-alternativa').textContent = alternativeDescription;

    // Mostrar botões de download e cópia
    document.getElementById('download-diagram').style.display = 'inline-block';
    document.getElementById('copy-diagram').style.display = 'inline-block';

    // Configurar botão de download
    document.getElementById('download-diagram').onclick = () => {
        const a = document.createElement('a');
        a.href = imagePath;
        a.download = 'diagrama.png';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        announceForScreenReader("Diagrama baixado com sucesso.");
    };
    
    // Configurar botão de copiar
    document.getElementById('copy-diagram').onclick = () => {
        const img = document.querySelector('#diagrama-container img');
        
        // Criar um canvas temporário para a conversão
        const canvas = document.createElement('canvas');
        canvas.width = img.naturalWidth;
        canvas.height = img.naturalHeight;
        
        // Desenhar a imagem no canvas
        const ctx = canvas.getContext('2d');
        ctx.drawImage(img, 0, 0);
        
        // Converter o canvas para blob e copiar para a área de transferência
        canvas.toBlob(blob => {
            navigator.clipboard.write([
                new ClipboardItem({'image/png': blob})
            ]).then(() => {
                announceForScreenReader("Imagem copiada para a área de transferência.");
            }).catch(err => {
                showError('diagram-error', 'Erro ao copiar imagem: ' + err.message);
            });
        });
    };
    
    // Anunciar para leitores de tela
    announceForScreenReader("Diagrama gerado com sucesso. A imagem está disponível com uma descrição alternativa.");
    
    // Rolar até a área do diagrama
    document.getElementById('result-section-title').scrollIntoView({ behavior: 'smooth' });
}

/**
 * Exibir mensagem de erro
 * @param {string} elementId - ID do elemento de erro
 * @param {string} message - Mensagem de erro
 */
function showError(elementId, message) {
    const element = document.getElementById(elementId);
    element.textContent = message;
    element.style.display = 'block';
    
    // Anunciar para leitores de tela
    announceForScreenReader(message);
    
    // Esconder a mensagem após um tempo
    setTimeout(() => {
        element.style.display = 'none';
    }, 5000);
}

/**
 * Mostrar ou esconder elemento de status
 * @param {string} elementId - ID do elemento de status
 * @param {boolean} show - Mostrar ou esconder
 */
function showStatus(elementId, show) {
    document.getElementById(elementId).style.display = show ? 'block' : 'none';
}

/**
 * Anunciar mensagem para leitores de tela usando ARIA live regions
 * @param {string} message - Mensagem a anunciar
 */
function announceForScreenReader(message) {
    // Criar um elemento temporário para o anúncio
    const announcement = document.createElement('div');
    announcement.setAttribute('aria-live', 'assertive');
    announcement.setAttribute('class', 'sr-only');
    announcement.textContent = message;
    
    document.body.appendChild(announcement);
    
    // Remover após um tempo para não sobrecarregar o DOM
    setTimeout(() => {
        document.body.removeChild(announcement);
    }, 3000);
}

// Garantir que o botão de copiar só apareça se a API estiver disponível
if (!navigator.clipboard || !navigator.clipboard.write) {
    document.getElementById('copy-diagram').style.display = 'none';
}
