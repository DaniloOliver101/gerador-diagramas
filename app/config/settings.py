"""
Project settings and configuration.
"""
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Upload folder for generated diagrams
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# OpenAI API configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    print("AVISO: OPENAI_API_KEY não está definida. As funcionalidades de IA estarão indisponíveis.")
    # Não levanta exceção para permitir que o aplicativo inicie, mas com funcionalidades limitadas

# Flask configuration
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    UPLOAD_FOLDER = UPLOAD_FOLDER