import os
import json
import requests
import logging
from flask import Blueprint, render_template, request, jsonify, current_app
from app.database import get_db_connection

# Configurar logging
logger = logging.getLogger(__name__)

# Crear el blueprint para merchandising
merchandising_bp = Blueprint('merchandising_bp', __name__, template_folder='../../templates')

# URL base de la API externa
API_BASE_URL = 'https://inventario-kssd.onrender.com'

@merchandising_bp.route('/merchandising/solicitud', methods=['GET'])
def solicitud_merchandising():
    """Muestra la página de solicitud de merchandising"""
    return render_template('merchandising/solicitud.html')

@merchandising_bp.route('/api/stock', methods=['GET'])
def obtener_stock():
    """Proxy para la API de stock"""
    grupo = request.args.get('grupo')
    if not grupo:
        return jsonify({"error": "Se requiere el parámetro 'grupo'"}), 400
    
    # Llamar a la API externa
    try:
        response = requests.get(f"{API_BASE_URL}/api/stock", params={"grupo": grupo})
        return jsonify(response.json()), response.status_code
    except Exception as e:
        logger.error(f"Error al obtener stock: {str(e)}")
        return jsonify({"error": "Error al obtener stock"}), 500

@merchandising_bp.route('/api/solicitud', methods=['POST'])
def crear_solicitud():
    """Proxy para crear una solicitud de merchandising"""
    if not request.is_json:
        return jsonify({"error": "Se esperaba JSON"}), 400
    
    data = request.get_json()
    
    # Validar campos requeridos
    required_fields = ['solicitante', 'grupo', 'ruc', 'fecha_visita', 'cantidad_packs', 'productos']
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"error": f"Campo requerido ausente: {field}"}), 400
    
    # Llamar a la API externa
    try:
        response = requests.post(f"{API_BASE_URL}/api/solicitud", json=data)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        logger.error(f"Error al crear solicitud: {str(e)}")
        return jsonify({"error": "Error al crear la solicitud"}), 500