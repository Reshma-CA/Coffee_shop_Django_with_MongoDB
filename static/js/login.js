document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const emailField = document.getElementById('email');
    const passwordField = document.getElementById('password');
    

    form.addEventListener('submit', function(event) {
        let isValid = true;

        // Clear previous error messages
        document.querySelectorAll('.error-message').forEach(el => el.textContent = '');

        // Check if fields are not empty
        if (!emailField.value.trim()) {
            isValid = false;
            document.getElementById('email-error').textContent = 'email is required.';
        }
        
        if (!passwordField.value.trim()) {
            isValid = false;
            document.getElementById('password-error').textContent = 'Password is required.';
        }
        


        if (!isValid) {
            event.preventDefault(); // Prevent form submission
        }
    });
});