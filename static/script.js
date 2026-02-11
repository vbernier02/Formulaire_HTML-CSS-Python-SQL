document.getElementById('loginFormulaireElement').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;
    const message = document.getElementById('loginMessage');
    
    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });
        
        const data = await response.json();
        
        if (data.success) {
            message.textContent = data.message;
            message.className = 'message success';
            document.getElementById('loginFormulaireElement').reset();
            setTimeout(() => {
                alert('Connexion au compte ' + username);
            }, 500);
        } else {
            message.textContent = data.message;
            message.className = 'message error';
        }
    } catch (error) {
        message.textContent = 'Erreur de connexion au serveur';
        message.className = 'message error';
    }
});

document.getElementById('signupFormulaireElement').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const username = document.getElementById('signupUsername').value;
    const password = document.getElementById('signupPassword').value;
    const confirmPassword = document.getElementById('signupConfirmPassword').value;
    const message = document.getElementById('signupMessage');
    
    try {
        const response = await fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                username, 
                password,
                confirm_password: confirmPassword 
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            message.textContent = data.message;
            message.className = 'message success';
            document.getElementById('signupFormulaireElement').reset();
            setTimeout(() => {
                showLogin();
            }, 1500);
        } else {
            message.textContent = data.message;
            message.className = 'message error';
        }
    } catch (error) {
        message.textContent = 'Erreur de connexion au serveur';
        message.className = 'message error';
    }
});

function showSignup() {
    document.getElementById('loginFormulaire').classList.remove('active');
    document.getElementById('signupFormulaire').classList.add('active');
    document.getElementById('signupMessage').textContent = '';
}

function showLogin() {
    document.getElementById('signupFormulaire').classList.remove('active');
    document.getElementById('loginFormulaire').classList.add('active');
    document.getElementById('loginMessage').textContent = '';
}

function resetFormulaire() {
    document.getElementById('loginFormulaireElement').reset();
    document.getElementById('loginMessage').textContent = '';
}
