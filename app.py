from app import create_app
import os
import logging

# Configuración de logging
logger = logging.getLogger(__name__)

# Crear la aplicación Flask
app = create_app()

if __name__ == '__main__':
    # Obtener el puerto del entorno o usar 5000 por defecto
    port = int(os.environ.get("PORT", 5001))
    
    # Ejecutar la aplicación en modo debug durante el desarrollo
    app.run(host='0.0.0.0', port=port, debug=True)
