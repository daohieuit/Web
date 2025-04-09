const buttonsToLogin = document.querySelectorAll('.redirect-to-login');

buttonsToLogin.forEach(button => {
    button.addEventListener('click', function() {
        const loginUrl = this.getAttribute('data-login-url');
        if (loginUrl) {
            window.location.href = loginUrl;
        }
    });
});