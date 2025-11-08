from flask import Flask, render_template, request, redirect, url_for, session, make_response
import json
import os
from datetime import timedelta

app = Flask(__name__)

# Use environment variable for secret key in production, fallback for development
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-for-production')
app.permanent_session_lifetime = timedelta(days=365)  # Session lasts 1 year

# File to store user data
DATA_FILE = 'users_data.json'

def load_users():
    """Load users from JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    """Save users to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(users, f, indent=2)

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """URL1: Registration page"""
    if request.method == 'POST':
        username = request.form.get('username')
        is_new_driver = request.form.get('is_new_driver') == 'yes'

        if username:
            users = load_users()
            users[username] = {
                'is_new_driver': is_new_driver
            }
            save_users(users)

            # Store username in permanent session (persists across browser sessions)
            session.permanent = True
            session['username'] = username

            return redirect(url_for('registration_success'))

    return render_template('register.html')

@app.route('/registration-success')
def registration_success():
    """Success page after registration"""
    return render_template('success.html')

@app.route('/status')
def status():
    """URL2: Automatically display driver status for recognized user"""
    driver_info = None
    username = None
    is_recognized = False

    # Automatically recognize user from session
    if 'username' in session:
        username = session['username']
        users = load_users()
        if username in users:
            driver_info = users[username]
            is_recognized = True

    return render_template('status.html',
                         username=username,
                         driver_info=driver_info,
                         is_recognized=is_recognized)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
