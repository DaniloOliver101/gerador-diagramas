"""
API routes for diagram generation.
"""
import uuid
from flask import Blueprint, request, jsonify, render_template, send_from_directory

from config.settings import UPLOAD_FOLDER
from core.diagram_manager import generate_diagram
from core.ai_service import generate_yaml_from_prompt


api_bp = Blueprint('api', __name__)


@api_bp.route('/')
def index():
    """
    Render the main application page.
    
    Returns:
        HTML rendered template
    """
    return render_template('index.html')


@api_bp.route('/generate_diagram', methods=['POST'])
def generate_diagram_route():
    """
    Generate a diagram from YAML data.
    
    Request JSON format:
        {
            "yaml_data": "YAML string for diagram generation"
        }
    
    Returns:
        JSON response with image path and alternative description, or error
    """
    try:
        yaml_data = request.json['yaml_data']
        if not yaml_data or not yaml_data.strip():
            return jsonify({'error': 'No YAML data provided'}), 400
            
        filename = str(uuid.uuid4())  # Unique identifier for the file
        
        image_path, alt_description, error = generate_diagram(yaml_data, filename)

        if error:
            return jsonify({'error': error}), 400
        
        return jsonify({
            'image_path': image_path,
            'alternative_description': alt_description
        })
    except KeyError:
        return jsonify({'error': 'Missing yaml_data field in request'}), 400
    except Exception as e:
        return jsonify({'error': f"Error processing request: {str(e)}"}), 500


@api_bp.route('/generate_yaml', methods=['POST'])
def generate_yaml_route():
    """
    Generate YAML from text description using AI.
    
    Request JSON format:
        {
            "prompt": "Description of the desired diagram"
        }
    
    Returns:
        JSON response with generated YAML, or error
    """
    try:
        prompt = request.json['prompt']
        if not prompt or not prompt.strip():
            return jsonify({'error': 'No prompt provided'}), 400
            
        yaml_content = generate_yaml_from_prompt(prompt)
        return jsonify({'yaml': yaml_content})
        
    except KeyError:
        return jsonify({'error': 'Missing prompt field in request'}), 400
    except Exception as e:
        return jsonify({'error': f"Error processing request: {str(e)}"}), 500


@api_bp.route('/static/uploads/<filename>')
def serve_diagram_file(filename):
    """
    Serve generated diagram files from the uploads directory.
    
    Args:
        filename (str): Name of the file to serve
        
    Returns:
        File response
    """
    return send_from_directory(UPLOAD_FOLDER, filename)