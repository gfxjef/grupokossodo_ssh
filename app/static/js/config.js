// Configuración global de la aplicación
const AppConfig = {
    // Ruta base de la aplicación (puede cambiar en producción)
    basePath: '',
    
    // Método para obtener la ruta completa
    getFullPath: function(path) {
        return this.basePath + path;
    },
    
    // API URLs
    apiUrls: {
        login: '/api/login',
        logout: '/api/logout'
    }
};
