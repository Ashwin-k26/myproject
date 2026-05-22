function toggleForms() {
    const loginForm = document.getElementById('loginForm');
    const signupForm = document.getElementById('signupForm');

    loginForm.classList.toggle('active');
    signupForm.classList.toggle('active');
}

function handleLogin(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    alert(`Welcome back, ${email}! You have successfully logged in.`);
    // Here you would typically send data to a server
    document.getElementById('loginForm').reset();
}

function handleSignup(event) {
    event.preventDefault();
    const fullname = document.getElementById('fullname').value;
    alert(`Welcome, ${fullname}! Your account has been created successfully.`);
    // Here you would typically send data to a server
    document.getElementById('signupForm').reset();
    toggleForms(); // Switch back to login form
}
