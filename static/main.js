const buttonsToLogin = document.querySelectorAll('.redirect-to-login');

buttonsToLogin.forEach(button => {
    button.addEventListener('click', function() {
        window.location.href = 'login.html';
    });
});