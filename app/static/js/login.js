document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('login-form');
    const errorMessage = document.getElementById('error-message');

    loginForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const usuario = document.getElementById('usuario').value;
        const pass = document.getElementById('pass').value;
        
        // Validación básica
        if (!usuario || !pass) {
            errorMessage.textContent = 'Por favor, ingrese usuario y contraseña';
            return;
        }
        
        // Enviar solicitud de login al servidor
        fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                usuario: usuario,
                pass: pass
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Guardar información del usuario en sessionStorage
                sessionStorage.setItem('userData', JSON.stringify(data.user));
                console.log('Datos de usuario guardados:', data.user);
                
                // Redirigir a la página de bienvenida
                window.location.href = '/api/welcome';
            } else {
                errorMessage.textContent = data.message || 'Error al iniciar sesión';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            errorMessage.textContent = 'Error de conexión. Intente nuevamente.';
        });
    });
});
