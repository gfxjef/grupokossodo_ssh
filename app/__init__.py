from flask import Flask
from dotenv import load_dotenv
import logging
import os

# Cargar variables de entorno
load_dotenv()

# Definir la ruta absoluta a la carpeta logs dentro de grupokossodo_ssh
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs')
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(log_dir, 'app.log')),
        logging.StreamHandler()
    ]
)

def create_app(config_name=None):
    """Inicializa la aplicación Flask"""
    app = Flask(__name__)
    
    # Configuración de la aplicación
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'clave_secreta_por_defecto')
    
    # Registro de blueprints
    from app.blueprints.login import get_blueprint as get_login_bp
    from app.blueprints.welcome import get_blueprint as get_welcome_bp
    from app.blueprints.records import get_blueprint as get_records_bp
    # Remove this line:
    # from app.blueprints.merchandising import get_blueprint as get_merchandising_bp
    from app.blueprints.inventory import get_blueprint as get_inventory_bp
    from app.blueprints.bienestar import get_blueprint as get_bienestar_bp
    from app.blueprints.bienestar import get_api_blueprint as get_bienestar_api_bp  # Import new function

    
    app.register_blueprint(get_login_bp(), url_prefix='/api')
    app.register_blueprint(get_welcome_bp(), url_prefix='/api')
    app.register_blueprint(get_records_bp())
    # Remove this line:
    # app.register_blueprint(get_merchandising_bp(), url_prefix='/api')
    app.register_blueprint(get_inventory_bp(), url_prefix='/api')
    app.register_blueprint(get_bienestar_bp(), url_prefix='/bienestar')
    app.register_blueprint(get_bienestar_api_bp(), url_prefix='/api')  # API endpoints under /api

    # Ruta principal que devuelve la aplicación frontend
    @app.route('/')
    def index():
        return app.send_static_file('index.html')
    
    @app.route('/health')
    def health():
        return {"status": "ok"}
    
    return app