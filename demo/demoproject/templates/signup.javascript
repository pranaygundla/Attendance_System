document.addEventListener("DOMContentLoaded", function() {
    
    // Get the form and its elements
    const form = document.querySelector("form");
    const emailInput = document.querySelector("input[type='email']");
    const passwordInput = document.querySelector("input[type='password']");
    const rememberMeCheckbox = document.querySelector("input[type='checkbox']");
    
    // Handle form submission
    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent default form submission
        
        // Validate email
        const email = emailInput.value.trim();
        const password = passwordInput.value.trim();

        // Regular expression for email validation
        const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        
        if (!email || !emailPattern.test(email)) {
            alert("Please enter a valid email address.");
            return; // Stop the form from submitting if email is invalid
        }

        // Validate password
        if (!password || password.length < 6) {
            alert("Password must be at least 6 characters long.");
            return; // Stop the form from submitting if password is invalid
        }

        // If both email and password are valid, show a success message
        if (rememberMeCheckbox.checked) {
            alert("Login successful. You will be remembered.");
        } else {
            alert("Login successful. You will not be remembered.");
        }

        // Optionally, reset the form after submission
        // form.reset(); 
    });
});
