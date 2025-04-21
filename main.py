import sys
import os
import logging

# Agregar el directorio actual al path de Python para que pueda encontrar el módulo app
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from app import create_app

# Configuración de logging
logger = logging.getLogger(__name__)

# Crear la aplicación Flask
app = create_app()

if __name__ == '__main__':
    # Obtener el puerto del entorno o usar 5000 por defecto
    port = int(os.environ.get("PORT", 5001))
    
    # Ejecutar la aplicación en modo debug durante el desarrollo
    app.run(host='0.0.0.0', port=port, debug=True)