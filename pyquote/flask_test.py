#!/usr/bin/env python
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = "Invalid username/password"
    return render_template('login.html', error=error)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the file']
        f.save('/var/uploads/upload_file.txt')


