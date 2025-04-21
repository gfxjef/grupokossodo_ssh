from flask import request, g

class PrefixMiddleware:
    """
    Middleware para manejar un prefijo de URL en la aplicación Flask
    cuando está montada bajo un prefijo en el DispatcherMiddleware
    """
    def __init__(self, app, prefix='/grupokossodo_ssh'):
        self.app = app
        self.prefix = prefix
        
    def __call__(self, environ, start_response):
        # Almacena el prefijo para que esté disponible en el contexto de la aplicación
        environ['SCRIPT_NAME'] = self.prefix
        # Actualiza el contexto de la aplicación
        return self.app(environ, start_response)