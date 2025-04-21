"""
Main application entry point.
"""
import os
from dotenv import load_dotenv
from flask import Flask
from waitress import serve

from api.routes import api_bp
from config.settings import Config, UPLOAD_FOLDER

# Load environment variables from .env file if it exists
# This doesn't override existing environment variables
load_dotenv(override=False)

def create_app():
    """
    Create and configure the Flask application.
    
    Returns:
        Flask: Configured Flask application
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register blueprints
    app.register_blueprint(api_bp)
    
    # Ensure upload folder exists
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    
    return app

if __name__ == '__main__':
    app = create_app()
    
    # Run development or production server based on environment
    if os.environ.get('FLASK_ENV') == 'development':
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        serve(app, host='0.0.0.0', port=5000)
        print("Server running in production mode on http://0.0.0.0:5000")