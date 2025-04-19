document.getElementById('gerar-diagrama').addEventListener('click', () => {
    const yamlInput = document.getElementById('yaml-input').value;

    fetch('/gerar_diagrama', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ yaml_data: yamlInput })
    })
    .then(response => response.json())
    .then(data => {
        if (data.erro) {
            alert("Erro ao gerar o diagrama: " + data.erro);
        } else {
            const imagemPath = data.imagem_path;
            const descricaoAlternativa = data.descricao_alternativa;

            const imgElement = `<img src="${imagemPath}" alt="${descricaoAlternativa}">`;
            document.getElementById('diagrama-container').innerHTML = imgElement;
            document.getElementById('descricao-alternativa').textContent = descricaoAlternativa;

            // Exibe os botões de download e copiar
            document.getElementById('download-diagram').style.display = 'inline-block';
            document.getElementById('copy-diagram').style.display = 'inline-block';

            // Configura o botão de download
            document.getElementById('download-diagram').onclick = () => {
                const a = document.createElement('a');
                a.href = imagemPath;
                a.download = 'diagrama.png'; // Nome do arquivo para download
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
            };

            // Configura o botão de copiar (abordagem alternativa)
            document.getElementById('copy-diagram').onclick = () => {
                const img = new Image();
                img.crossOrigin = "anonymous";
                img.onload = function () {
                    const canvas = document.createElement("canvas");
                    canvas.width = img.width;
                    canvas.height = img.height;
                    const ctx = canvas.getContext("2d");
                    ctx.drawImage(img, 0, 0);
                    canvas.toBlob(blob => {
                        navigator.clipboard.write([
                            new ClipboardItem({
                                "image/png": blob
                            })
                        ]).then(() => {
                            alert("Imagem copiada para a área de transferência!");
                        }).catch(err => {
                            console.error("Falha ao copiar imagem: ", err);
                            alert("Falha ao copiar imagem. Por favor, use o download.");
                        });
                    }, "image/png");
                };
                img.src = imagemPath;
            };
        }
    })
    .catch(error => {
        console.error('Erro na requisição:', error);
        alert('Ocorreu um erro ao gerar o diagrama.');
    });
});