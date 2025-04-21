// Verificación de autenticación
document.addEventListener('DOMContentLoaded', function() {
    // Verificar si existe información del usuario en sessionStorage
    const userData = JSON.parse(sessionStorage.getItem('userData') || 'null');
    
    // Si no hay datos de usuario, redirigir al login
    if (!userData) {
        console.log('No se encontró información de usuario. Redirigiendo al login...');
        // Redirigir a la página de login
        window.location.href = '/api/login';
        return;
    }
    
    console.log('Usuario autenticado:', userData.nombre);
});
