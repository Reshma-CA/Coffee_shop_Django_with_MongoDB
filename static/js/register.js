document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const usernameField = document.getElementById('username');
    const emailField = document.getElementById('email');
    const passwordField = document.getElementById('password');
    const confirmPasswordField = document.getElementById('confirm-password');

    form.addEventListener('submit', function(event) {
        let isValid = true;

        // Clear previous error messages
        document.querySelectorAll('.error-message').forEach(el => el.textContent = '');

        // Check if fields are not empty
        if (!usernameField.value.trim()) {
            isValid = false;
            document.getElementById('username-error').textContent = 'Username is required.';
        }
        if (!emailField.value.trim()) {
            isValid = false;
            document.getElementById('email-error').textContent = 'Email is required.';
        }
        if (!passwordField.value.trim()) {
            isValid = false;
            document.getElementById('password-error').textContent = 'Password is required.';
        }
        if (!confirmPasswordField.value.trim()) {
            isValid = false;
            document.getElementById('confirm-password-error').textContent = 'Please confirm your password.';
        }

        // Validate email format
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (emailField.value && !emailPattern.test(emailField.value)) {
            isValid = false;
            document.getElementById('email-error').textContent = 'Invalid email format.';
        }

        // Password validation rules
        const passwordValue = passwordField.value;
        const passwordPattern = /^(?=.*[A-Z])(?=.*[0-9])(?=.*[@#^$!%*?&])[A-Za-z\d@#^$!%*?&]{8,}$/;

        if (passwordValue) {
            if (!passwordPattern.test(passwordValue)) {
                isValid = false;
                document.getElementById('password-error').textContent = 'Password must be at least 8 characters long, contain an uppercase letter, a number, and a special character (e.g., @, #, !).';
            }
        }

        // Validate passwords match
        if (passwordValue && confirmPasswordField.value !== passwordValue) {
            isValid = false;
            document.getElementById('confirm-password-error').textContent = 'Passwords do not match.';
        }

        if (!isValid) {
            event.preventDefault(); // Prevent form submission
        }
    });
});