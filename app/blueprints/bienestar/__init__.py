# In app/blueprints/bienestar/__init__.py
from app.blueprints.bienestar.routes import bienestar_bp
from app.blueprints.bienestar.api import bienestar_api_bp  # New API blueprint

def get_blueprint():
    return bienestar_bp

def get_api_blueprint():  # New function
    return bienestar_api_bp