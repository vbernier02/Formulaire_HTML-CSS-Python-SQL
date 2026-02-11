from flask import Flask, render_template, request, jsonify, session
import bcrypt
import sqlite3
import os
import re

formulaire = Flask(__name__)
formulaire.secret_key = 'placeholder_key'


DB_FILE = "data_user.db"

def init_database():
    if not os.path.exists(DB_FILE):
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        '''
        )
            cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", ("test", hash_password("test")))

def hash_password(password):
    hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hash.decode()

def check_password(hash, password):
    try:
        return bcrypt.checkpw(password.encode(), hash.encode())
    except Exception:
        return False

def validate_username(username):
    regex = r'^[a-zA-Z0-9_]{3,15}$'
    return re.match(regex, username) is not None

@formulaire.route('/')
def index():
    return render_template('index.html')

@formulaire.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()
    
    if not username:
        return jsonify({'success': False, 'message': 'Veuillez entrer un identifiant'})

    if not validate_username(username):
        return jsonify({'success': False, 'message': 'Identifiant invalide'})

    if not password: 
        return jsonify({'success': False, 'message': 'Veuillez entrer un mot de passe'})
    
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()

    if result and check_password(result[0], password):
        session['username'] = username
        return jsonify({'success': True, 'message': 'Connexion réussie'})
    else:
        return jsonify({'success': False, 'message': 'Identifiant ou mot de passe incorrect'})

@formulaire.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()
    confirm_password = data.get('confirm_password', '').strip()
    
    if not username:
        return jsonify({'success': False, 'message': 'Veuillez entrer un identifiant'})
    
    if not validate_username(username):
        return jsonify({'success': False, 'message': 'Identifiant invalide'})
    
    if password != confirm_password:
        return jsonify({'success': False, 'message': 'Les mots de passe ne correspondent pas'})
    
    try:
        with sqlite3.connect(DB_FILE) as conn:
            conn.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                         (username, hash_password(password)))
        return jsonify({'success': True, 'message': 'Compte créé'})
    except sqlite3.IntegrityError:
        return jsonify({'success': False, 'message': 'Cet identifiant existe déjà'})

if __name__ == '__main__':
    init_database()
    formulaire.run(debug=True, host='localhost', port=5000)